import _thread
import time
from machine import Pin, I2C

## Variables:
time_threshold = 3  # Time interval to wait before allowing input to stop the loop. This prevents the loop from stopping imidiatly after starting, as the powersource will still be on.
output_file_name = 'TEST.log' #Name of file where measurements are written to.
dt = 0.01 # Time between measurements.
minimal_length_impuls = 0.01 #Time interval in which to check the trigger pin.
printer_stand_still= 1 #In the printer code, you have to stop the arm after fan starts, so this is to compensate for that.

loop1_running = False
last_transition_time = None  # Track the time of the last 0-to-1 transition
lock = _thread.allocate_lock()  # Lock for thread synchronization

# Pin object for controlling onboard LED
led = Pin("LED", Pin.OUT)

# Pin for I2C communication
sdaPIN = Pin(16)
sclPIN = Pin(17)
i2c = I2C(0, sda=sdaPIN, scl=sclPIN, freq=210000)

# Pin for the trigger signal
trig = Pin(11, Pin.IN, Pin.PULL_DOWN)
powersource = Pin(4, Pin.OUT)
powersource.on()

# I2C sensor address
addr = 0x35

# Function to write header to the log file
def write_header():
    with open(output_file_name, 'w') as f:  # Use 'w' to overwrite the file
        f.write("t  x  y  z\n")

# Initialize sensor
def init_sensor():
    i2c.writeto(addr, b'\x00\x20')  # Device config 1
    i2c.writeto(addr, b'\x01\x22')  # Device config 2
    i2c.writeto(addr, b'\x02\x79')  # Sensor config 1
    i2c.writeto(addr, b'\x07\x01')  # Temp config

# Monitor the signal (Trigger signal) in the main thread
def monitor_signal():
    global loop1_running, last_transition_time
    
    while True:
        if trig.value() == 1:
            current_time = time.time()
            # Start Loop 1 if not running
            if not loop1_running:
                lock.acquire()
                loop1_running = True
                last_transition_time = current_time
                lock.release()
                print("Measuring started")
                # Start loop1 in a new thread
                _thread.start_new_thread(loop1, ())
                
            
            # Stop Loop 1 after time threshold
            elif loop1_running and (current_time - last_transition_time >= time_threshold):
                lock.acquire()
                loop1_running = False
                print("Measuring stopped")
                last_transition_time = None  # Reset transition time
                lock.release()
            
            time.sleep(time_threshold)  # Debounce delay
        
        time.sleep(minimal_length_impuls)  # Short delay to avoid rapid polling for second start

# Main data collection loop
def loop1():
    global loop1_running
    t = 0  # Start timestamp relative to loop start
    time.sleep(printer_stand_still)
    with open(output_file_name, 'a') as f:# Open the file once in append mode
        f.write("\n")
        while loop1_running:
            start = time.time()  # Record start time of the iteration
            led.value(1)  # Turn on the LED (for visualization)
            
            print(t)
            s = i2c.readfrom_mem(addr, 0x12, 0x17)  # Read Hall effect sensor data
            x = ((s[0x12-0x12] << 4) + (s[0x13-0x12] >> 4))
            y = ((s[0x14-0x12] << 4) + (s[0x15-0x12] >> 4))
            z = ((s[0x16-0x12] << 4) + (s[0x17-0x12] >> 4))
                
                # Adjust negative values
            if x > 2048:
                x -= 4096
            if y > 2048:
                y -= 4096
            if z > 2048:
                z -= 4096
                
                # Write data to file with timestamp
            f.write(f"{t:.3f} {x:+03d} {y:+03d} {z:+03d}\n")
         
            # Calculate elapsed time and update timestamp
            elapsed = time.time() - start
            t += elapsed
            t += dt
            # Wait for the next sampling point
            time.sleep(dt)
        
        led.value(0)  # Turn off the LED after loop stops
        print("Loop 1 finished")
        
        

# Main function
def main():
    write_header()  # Write header to log file
    init_sensor()  # Initialize the sensor
    monitor_signal()  # Start monitoring signal in the main thread

# Run the main function
main()