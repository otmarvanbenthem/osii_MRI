"""Code to compute optimized permanent magnet shim for a permanent low-field MRI magnet.

Stephen Ogier - October 2024

At present, this code only uses the Z-component of the shim output
    It could be expanded to work with 3-axis b0 map data.
"""

import numpy as np
import pandas as pd
import magpylib as magpy
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt
import csv
import pickle

from pymoo.optimize import minimize
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import RankAndCrowdingSurvival
from pymoo.core.variable import Choice, Binary
from pymoo.core.mixed import MixedVariableGA

import logging

from multiprocessing.pool import ThreadPool
from pymoo.core.problem import StarmapParallelization

import time

# Specify files with input data
mag_pos_fname = 'example_data/OSII_MINI.csv'
b0_map_fname = 'example_data/NIST_Smallbach_Swap_Smoothed_shell.csv'

# Configuration Options
n_threads = 8
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

B0_nom = .04567 # T

# Define magnet properties
s = 0.003   
cube_dims = (s,s,s)
cube_mag = (0,0,1185704) # N56 magnet average 
logging.info(f'Magnets are cubes with side length {s*1e3} mm')
logging.info(f'Magnets have magnetization {cube_mag} A/m')

# Define optimization options
n_angles = 4
angles = list(np.linspace(0,2*np.pi,n_angles,endpoint=False))

# Begin execution
start_time = time.time()

# Set up Multi-threading
pool = ThreadPool(n_threads)
runner = StarmapParallelization(pool.starmap)

def magnet_pos_angle_import(magnet_pos_fname):
    """Import CSV file of magnet positions.
    CSV has following format:
    X   Y   Z   Angle
    x0  y0  z0  a0
    x1  y1  z1  a1
    ...

    where (x,y,z) is relative to isocenter of magnet
    and Angle is rotation about X axis
    Magnetization is assumed to be along Z
    """
    magnet_pos_angle_df = pd.read_csv(magnet_pos_fname, header=0, names=['X','Y','Z','Angle'])
    logging.info(f'Successful import of magnet position+angle specification: {magnet_pos_fname}')
    return magnet_pos_angle_df

def magnet_pos_import(magnet_pos_fname):
    """Import CSV file of magnet positions.
    CSV has following format:
    X   Y   Z
    x0  y0  z0
    x1  y1  z1
    ...

    where (x,y,z) is relative to isocenter of magnet
    Magnetization is assumed to be along Z
    """
    magnet_pos_df = pd.read_csv(magnet_pos_fname, header=0, names=['X','Y','Z'])
    logging.info(f'Successful import of magnet position+angle specification: {magnet_pos_fname}')
    return magnet_pos_df

def b0_map_import(b0_map_fname, l_unit = 'mm'):
    """Import B0 map CSV file.
    CSV has the following format:
    X   Y   Z   B0
    x0  y0  z0  B0_0
    x1  y1  z1  B0_1
    ...

    All columns after B0 are ignored.
    """
    b0_map_df = pd.read_csv(b0_map_fname, header=0, usecols=[0,1,2,3], names=['X','Y','Z','B0'])
    logging.info(f'Successful import of B0 map: {b0_map_fname}')
    if l_unit == 'mm':
        b0_map_df['X'] = b0_map_df['X'].values*1e-3
        b0_map_df['Y'] = b0_map_df['Y'].values*1e-3
        b0_map_df['Z'] = b0_map_df['Z'].values*1e-3
    return b0_map_df

def generate_magnets(mag_pos_angle):
    """Generate collection of magnets from array of positions
    mag_pos_angle is a Nx4 array with the following format
        x0  y0  z0  angle0
        x1  y1  z1  angle1
    """
    mag_pos = mag_pos_angle[:,:3]
    angles = mag_pos_angle[:,3]
    mag_rot = R.from_euler('x', angles)

    n_magnets = mag_pos.shape[0]

    magnets = magpy.Collection(style_label='magnets')

    for i in range(n_magnets):
        cube = magpy.magnet.Cuboid(position=mag_pos[i,:], orientation=mag_rot[i], dimension=cube_dims, magnetization=cube_mag)
        magnets.add(cube)
    
    return magnets

def generate_grid_YZ(side, npoints):
    """Generate a grid in the YZ plane (at X=0) for plotting fields

    side is length of side of grid in m
    npoints is number of points in grid along Y and Z
    """
    axis = np.linspace(-side/2, side/2, npoints)
    grid = np.array([[(0,y,z) for y in axis] for z in axis])
    return grid

def compute_fields(mag_pos_angle, sensors):
    """Compute fields of magnets specified in sensor array
    mag_pos_angle is a Nx4 array with the following format
        x0  y0  z0  angle0
        x1  y1  z1  angle1
        ...
    sensor_pos is a Nx3 array with the following format
        x0  y0  z0
        x1  y1  z1
        ...
    """
    # Generate magnet position and rotation
    magnets = generate_magnets(mag_pos_angle)
    
    B = magnets.getB(sensors)
    return B

def compute_cost(mag_pos_angle, sensors: magpy.Sensor, b0_map_vals):
    """Compute cost function for optimization

    Cost function is presently std dev of sum of shim B field and the b0 map in ppm
    """
    if len(mag_pos_angle) == 0:
        cost = np.std(b0_map_vals)
    else:
        B_shim = compute_fields(mag_pos_angle, sensors)
        B_combined = B_shim[:,2]+b0_map_vals # Add Z-component of shim fields to mapped magnet
        cost = np.std(B_combined,0)

    cost = cost/B0_nom*1e6
    
    print(f'Cost: {cost:.0f} ppm')
    return cost

class ShimProblem(ElementwiseProblem):
    """Define problem for shimming GA optimization"""
    def __init__(self, magnet_pos_df:pd.DataFrame, b0_map_df:pd.DataFrame, **kwargs):
        """Initialize GA"""

        # Convert from Pandas dfs to numpy arrays
        self.magnet_pos = magnet_pos_df.to_numpy()[:,:3]
        
        sensor_pos = b0_map_df.to_numpy()[:,:3]
        
        # Generate Sensors. They can be encasulated in the ShimProblem, as their location never changes
        n_sensors = sensor_pos.shape[0]
        
        self.sensors = magpy.Collection(style_label='sensors')
        for i in range(n_sensors):
            sensor = magpy.Sensor(sensor_pos[i,:])
            self.sensors.add(sensor)

        self.b0_map_vals = b0_map_df.to_numpy()[:,3]

        self.n_magnets = self.magnet_pos.shape[0] # Number of possible magnet positions

        logging.info(f'Optimizing {self.n_magnets} magnets')
        # Initialize dictionary of variables to optimize
        variables = dict()
        for i in range(self.n_magnets):
            # For each magnet, there are two variables
            # A binary variable for whether the magnet should be there
            variables[f'binary___{i:04}'] = Binary()
            # And a choice for the angle of the magnet
            variables[f'rotation_{i:04}'] = Choice(options=angles)

        super().__init__(vars=variables, n_ieq_contr=0, n_obj=1, **kwargs)

    def _evaluate(self, X, out, *args, **kwargs):
        # Extract magnet placement variables from X

        mag_binary = np.array([X[f'binary___{i:04}'] for i in range(self.n_magnets)])
        mag_angles = np.array([X[f'rotation_{i:04}'] for i in range(self.n_magnets)])

        # for i in range(self.n_magnets):
        #     print(f'Magnet {i:04} {mag_binary[i]} {mag_angles[i]}')

        mag_pos_angle = np.concatenate((self.magnet_pos[mag_binary,:], mag_angles[mag_binary, None]),1)
        
        out["F"] = compute_cost(mag_pos_angle, self.sensors, self.b0_map_vals)
        # pr.dump_stats('profile.txt')

magnet_pos_df = magnet_pos_import(mag_pos_fname)
b0_map_df = b0_map_import(b0_map_fname)

unshimmed_homogeneity = np.std(b0_map_df.to_numpy()[:,3])/B0_nom*1e6
print(f'Unshimmed Homogeneity: {unshimmed_homogeneity:.0f} ppm')

problem = ShimProblem(magnet_pos_df, b0_map_df, elementwise_runner=runner)

algorithm = MixedVariableGA(pop_size=100, survival=RankAndCrowdingSurvival())
result = minimize(problem, algorithm, ('n_gen', 10), verbose=True)
pool.close()

print("--- %s seconds ---" % (time.time() - start_time))

X = result.X
mag_binary = np.array([X[f'binary___{i:04}'] for i in range(problem.n_magnets)])
mag_angles = np.array([X[f'rotation_{i:04}'] for i in range(problem.n_magnets)])

with open('shim_out.csv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='excel')
    writer.writerow(['X', 'Y', 'Z', 'Place', 'Angle'])
    for i in range(problem.n_magnets):
        writer.writerow([*problem.magnet_pos[i,:], mag_binary[i], mag_angles[i]])

with open('optimization_results.pickle', 'wb') as f:
    pickle.dump(result)
