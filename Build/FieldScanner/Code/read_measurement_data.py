# -*- coding: utf-8 -*-
"""
This code turns the photosensor measurements into a speed profile for our robotic arm.
"""

from scipy import signal
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


#File path and file name of measurements.
file_name= 'V_TEST_2.log'
path = Path("C:/Users/otmar/Downloads/" )
file_to_open = path / file_name

#Data.
data_file  = np.loadtxt(file_to_open, skiprows=1, dtype='float') 
data_file = data_file.T #array of date, where index 0 is the time stamp and index 1 is the measurement
data_file=np.array(data_file)

t= data_file[0]
split = np.delete(np.array(np.where(t ==0))[0],0)
V= data_file[1]

t=np.split(t,split)
print(t[0])
V=np.split(V,split)
plt.figure()
plt.plot(t[0],V[0])
plt.show()


#%%

z=np.zeros(len(t[0]))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with intensity
scatter = ax.scatter(z, z, t[0], c=V[0], cmap='viridis', s=200)

# Add a colorbar
colorbar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=10)
colorbar.set_label('Intensity')

# Add labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('t(z)')

ax.set_box_aspect(aspect=(2, 2, 5), zoom=1)
plt.show()


        
        
        
        
    
    

