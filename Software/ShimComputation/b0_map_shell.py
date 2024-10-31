"""
Reduce fully sampled B0 map to just outermost shell

@author: seogier
"""
import numpy as np
import matplotlib.pyplot as plt

path_full = 'example_data/NIST_Smallbach_Swap_Smoothed.csv'
path_out = 'example_data/NIST_Smallbach_Swap_Smoothed_shell.csv'

min_rad = 45 # mm
full = np.genfromtxt(path_full, dtype = float, delimiter = ',', skip_header = 1)

mask = np.sqrt(full[:,0]**2 + full[:,1]**2 + full[:,2]**2) > min_rad

shell = full[mask,:]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(shell[:,0], shell[:,1], shell[:,2], c = shell[:,3], cmap = 'viridis')
ax.set_xlabel("X [mm] Bore direction")
ax.set_ylabel("Y [mm] (up down)")
ax.set_zlabel("Z [mm] (B0)")
fig.suptitle('Fitted data')
plt.show()

print(f'Went from {np.shape(full)[0]} to {np.shape(shell)[0]} points')

np.savetxt(path_out, shell, delimiter=',', header='X,Y,Z,B0,Bx,By,Bz')