import random

import matplotlib
import numpy as np
import generator_shape as gn
import matplotlib.pyplot as plt
import dist_eval as evl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import math

#spehere: 162,642,2562 #change radius as well

#mesh1 = gn.sphere_generator(9.5, 162)
#mesh2 = gn.sphere_generator(10, 162)

radius = random.randint(0,100)
noise = radius/100
num_points = 625 #spehere: 162,642,2562 #change radius as well

#169, 625, 2500

mesh1 = gn.sphere_generator(radius, num_points, noise)

if radius%2 == 0:
    mesh2 = gn.sphere_generator(radius-noise, num_points, 0)
else:
    mesh2 = gn.sphere_generator(radius+noise, num_points, 0)



#mesh1 = gn.sphere_generator(7.5, 2542)
#mesh2 = gn.sphere_generator(10, 2562)


#Target Mesh
fig0 = plt.figure()
ax0 = fig0.add_subplot(111, projection='3d')
ax0.set_title("Target Mesh")

u, v = np.mgrid[0:2*np.pi:math.sqrt(num_points)*1j, 0:np.pi:math.sqrt(num_points)*1j]
x = radius*np.cos(u)*np.sin(v)
y = radius*np.sin(u)*np.sin(v)
z = radius*np.cos(v)

ax0 = ax0.scatter3D(x, y, z, s=50)

#RMS Heat Map without Normalize
# rms_dis = evl.rms_without_normalize(mesh1, mesh2)
#
# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111, projection='3d')
# ax2.set_title("RMS Heat Map without Normalize - RMS Score: "+ str(sum(rms_dis)/len(rms_dis)))
#
# xtest = mesh1[:, 0]
# ytest = mesh1[:, 1]
# ztest = mesh1[:, 2]
#
# ax2 = ax2.scatter3D(xtest, ytest, ztest, c=rms_dis, cmap='Spectral_r', s=50);
#
# fig2.colorbar(ax2)
#
# #RMS Heat Map with Normalize
# rms_dis_w_no = evl.rms_with_normalize(mesh1, mesh2)
#
# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111, projection='3d')
# ax2.set_title("RMS Heat Map with Normalize - RMS Score: "+ str(sum(rms_dis_w_no)/len(rms_dis_w_no)))
#
# xtest = mesh1[:, 0]
# ytest = mesh1[:, 1]
# ztest = mesh1[:, 2]
#
# ax2 = ax2.scatter3D((xtest - np.min(xtest)) / np.ptp(xtest), (ytest - np.min(ytest)) / np.ptp(ytest), (ztest - np.min(ztest)) / np.ptp(ztest), c=rms_dis_w_no, cmap='Spectral_r', s=50);
#
# fig2.colorbar(ax2)

#Chamfer Heat Map without Normalize
cham_dis = evl.chamfer_without_normalize(mesh1, mesh2)

fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection='3d')
ax3.set_title("Chamfer Heat Map without Normalize - Chamfer Score: "+ str(sum(cham_dis)/len(cham_dis)))

xtest = mesh1[:, 0]
ytest = mesh1[:, 1]
ztest = mesh1[:, 2]

ax3 = ax3.scatter3D(xtest, ytest, ztest, c=cham_dis, cmap='Spectral_r', s=50);

fig3.colorbar(ax3)

#Uniform Chamfer Heat Map without Normalize

u, v = np.mgrid[0:2*np.pi:math.sqrt(num_points)*1j, 0:np.pi:math.sqrt(num_points)*1j]
x = radius*np.cos(u)*np.sin(v)
y = radius*np.sin(u)*np.sin(v)
z = radius*np.cos(v)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.set_title("Chamfer Heat Map without Normalize - Chamfer Score: "+ str(sum(cham_dis)/len(cham_dis)))

color_dimension = np.reshape(cham_dis,(int(math.sqrt(num_points)),int(math.sqrt(num_points)))) # change to desired fourth dimension
minn, maxx = color_dimension.min(), color_dimension.max()
norm = matplotlib.colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='Spectral_r')
m.set_array([])
fcolors = m.to_rgba(color_dimension)

ax2.plot_surface(x, y, z, facecolors=fcolors,alpha=1)

fig2.colorbar(m)

#Chamfer Heat Map with Normalize
cham_dis_w_no = evl.chamfer_with_normalize(mesh1, mesh2)

fig4 = plt.figure()
ax4 = fig4.add_subplot(111, projection='3d')
ax4.set_title("Chamfer Heat Map with Normalize - Chamfer Score: "+ str(sum(cham_dis_w_no)/len(cham_dis_w_no)))

xtest = mesh1[:, 0]
ytest = mesh1[:, 1]
ztest = mesh1[:, 2]

ax4 = ax4.scatter3D((xtest - np.min(xtest)) / np.ptp(xtest), (ytest - np.min(ytest)) / np.ptp(ytest), (ztest - np.min(ztest)) / np.ptp(ztest), c=cham_dis_w_no, cmap='Spectral_r', s=50);

fig4.colorbar(ax4)

# Uniform Chamfer Heat Map with Normalize

u, v = np.mgrid[0:2*np.pi:math.sqrt(num_points)*1j, 0:np.pi:math.sqrt(num_points)*1j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)

fig5 = plt.figure()
ax5 = fig5.gca(projection='3d')
ax5.set_aspect("equal")



ax5.set_title("Chamfer Heat Map with Normalize - Chamfer Score: "+ str(sum(cham_dis_w_no)/len(cham_dis_w_no)))

color_dimension = np.reshape(cham_dis_w_no,(int(math.sqrt(num_points)),int(math.sqrt(num_points)))) # change to desired fourth dimension
minn, maxx = color_dimension.min(), color_dimension.max()
norm = matplotlib.colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='Spectral_r')
m.set_array([])
fcolors = m.to_rgba(color_dimension)

ax5.plot_surface(x, y, z, facecolors=fcolors,alpha=1)

fig5.colorbar(m)

plt.show()