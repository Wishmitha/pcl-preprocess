from math import sqrt
import random
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def sphere_generator(radius, num_points):

    surface_coord = []

    for i in range(num_points):
        x = random.uniform(-100,100)
        y = random.uniform(-100,100)
        z = random.uniform(-100,100)
        
        points = np.zeros(shape=(3,));

        points[0] = x;
        points[1] = y;
        points[2] = z;

        points = points * radius/sqrt(x*x+y*y+z*z)

        surface_coord.append(points)

    return np.array(surface_coord)


def cube_generator(length, num_points):

    surface_coord = []

    for i in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        z = random.uniform(0, 1)

        face = random.randint(0,6)

        if(face == 0):
            x = 0
        elif(face ==1):
            x = 1
        elif(face==2):
            y = 0
        elif (face == 3):
            y = 1
        elif (face == 4):
            z = 0
        elif (face == 5):
            z = 1

        points = np.zeros(shape=(3,));

        points[0] = x;
        points[1] = y;
        points[2] = z;

        surface_coord.append(points)

    return np.array(surface_coord)

some = cube_generator(10,10000)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



# Data for three-dimensional scattered points

xdata = some[:,0]
ydata = some[:,1]
zdata = some[:,2]

ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens', s=2);

plt.show()




