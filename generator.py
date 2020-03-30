import numpy as np
import random
import pcl
from  planar__projection import project

def generate(cloud):

    cloud_array = np.asarray(cloud)

    gen_cloud_list = []

    for point in cloud_array:
        gen_cloud_list.append(point + random.randrange(-50,50,1))

    gen_cloud_list = np.array(gen_cloud_list, dtype=np.float32)
    return pcl.PointCloud(gen_cloud_list)

def rnd_generate(cloud):

    cloud_array = np.asarray(cloud)

    gen_cloud_list = []

    for point in cloud_array:
        points= []

        points.append(point[0] + random.randrange(-50, 50, 1))
        points.append(point[1] + random.randrange(-50, 50, 1))
        points.append(point[2] + random.randrange(-50, 50, 1))

        gen_cloud_list.append(points)

    gen_cloud_list = np.array(gen_cloud_list, dtype=np.float32)
    return pcl.PointCloud(gen_cloud_list)

def pro_generate(cloud):
    pro_cloud = project(cloud, [1,1,1,0])

    cloud_array = np.asarray(pro_cloud)

    pro_cloud_list = []

    for point in cloud_array:
        points = []

        points.append(point[0] + random.randrange(-50, 50, 1))
        points.append(point[1] + random.randrange(-50, 50, 1))
        points.append(point[2]+ random.randrange(-50, 50, 1))

        pro_cloud_list.append(points)

    pro_cloud_list = np.array(pro_cloud_list, dtype=np.float32)
    print(pro_cloud_list)
    return pcl.PointCloud(pro_cloud_list)


