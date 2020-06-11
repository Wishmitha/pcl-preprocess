import random

import matplotlib
import numpy as np
import generator_shape as gn
import matplotlib.pyplot as plt
import dist_eval as evl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import math

f1 = open("foot_xyz/generated.xyz", "r")
gen_list_str = f1.read().split('\n')

gen_list=[]

for x in gen_list_str:
    gen_list.append(x.split())

gen = np.array(gen_list)

gen = gen[:,:3]

f2 = open("foot_xyz/sampled.xyz", "r")
sam_list_str = f2.read().split('\n')

sam_list=[]

for x in sam_list_str:
    sam_list.append(x.split())

sam = np.array(sam_list)

sam = sam[:,:3]

#surface viz gen

x = gen[:,0].reshape(81,1)
y = gen[:,1].reshape(81,1)
z = gen[:,2].reshape(81,1)

print(x,y,z)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
#ax2.set_title("Chamfer Heat Map without Normalize - Chamfer Score: "+ str(sum(cham_dis)/len(cham_dis)))

#color_dimension = np.reshape(cham_dis,(int(math.sqrt(num_points)),int(math.sqrt(num_points)))) # change to desired fourth dimension
#minn, maxx = color_dimension.min(), color_dimension.max()
#norm = matplotlib.colors.Normalize(minn, maxx)
#m = plt.cm.ScalarMappable(norm=norm, cmap='Spectral_r')
#m.set_array([])
#fcolors = m.to_rgba(color_dimension)

ax2.plot_surface(x, y, z)
plt.show()

#fig2.colorbar(m)