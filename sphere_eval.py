import random

import matplotlib
import numpy as np
import generator_shape as gn
import matplotlib.pyplot as plt
import dist_eval as evl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

#spehere: 162,642,2562 #change radius as well

#mesh1 = gn.sphere_generator(9.5, 162)
#mesh2 = gn.sphere_generator(10, 162)

radius = random.randint(0,100)
noise = radius/100
num_points = 162 #spehere: 162,642,2562 #change radius as well

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

xtrg = mesh2[:, 0]
ytrg = mesh2[:, 1]
ztrg = mesh2[:, 2]

ax0 = ax0.scatter3D(xtrg, ytrg, ztrg, s=1)

#RMS Heat Map without Normalize
rms_dis = evl.rms_without_normalize(mesh1, mesh2)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.set_title("RMS Heat Map without Normalize - RMS Score: "+ str(sum(rms_dis)/len(rms_dis)))

xtest = mesh1[:, 0]
ytest = mesh1[:, 1]
ztest = mesh1[:, 2]

ax2 = ax2.scatter3D(xtest, ytest, ztest, c=rms_dis, cmap='Spectral_r', s=50);

fig2.colorbar(ax2)

#RMS Heat Map with Normalize
rms_dis_w_no = evl.rms_with_normalize(mesh1, mesh2)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.set_title("RMS Heat Map with Normalize - RMS Score: "+ str(sum(rms_dis_w_no)/len(rms_dis_w_no)))

xtest = mesh1[:, 0]
ytest = mesh1[:, 1]
ztest = mesh1[:, 2]

ax2 = ax2.scatter3D((xtest - np.min(xtest)) / np.ptp(xtest), (ytest - np.min(ytest)) / np.ptp(ytest), (ztest - np.min(ztest)) / np.ptp(ztest), c=rms_dis_w_no, cmap='Spectral_r', s=50);

fig2.colorbar(ax2)

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

# uniform

fig5 = plt.figure()
ax5 = fig5.gca(projection='3d')
ax5.set_aspect("equal")

u, v = np.mgrid[0:2*np.pi:18j, 0:np.pi:9j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)



#ax5.scatter(x, y, z, c=cham_dis_w_no,cmap='Spectral_r',s=100)
#print(cham_dis_w_no)
#cham_dis_w_no = np.reshape(cham_dis_w_no,(169,1))
#print(cham_dis_w_no)

color_dimension = np.reshape(cham_dis_w_no,(18,9)) # change to desired fourth dimension
minn, maxx = color_dimension.min(), color_dimension.max()
norm = matplotlib.colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='Spectral_r')
m.set_array([])
fcolors = m.to_rgba(color_dimension)

print(fcolors.shape)

ax5.plot_surface(x, y, z, facecolors=fcolors,alpha=1)

fig5.colorbar(m)

plt.show()