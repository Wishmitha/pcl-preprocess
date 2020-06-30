import numpy as np
import random
import math

radius = random.randint(0,100)
noise = radius/100
num_points = 2500 #spehere: 162,642,2562 #change radius as well

u, v = np.mgrid[0:2*np.pi:math.sqrt(num_points)*1j, 0:np.pi:math.sqrt(num_points)*1j]
x = radius*np.cos(u)*np.sin(v)
y = radius*np.sin(u)*np.sin(v)
z = radius*np.cos(v)
