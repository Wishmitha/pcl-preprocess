import pcl
import numpy as np


def project(cloud, coefficients):

    normal = np.array(coefficients[:-1])

    cloud_array = np.asarray(cloud)

    projected_cloud_list = []

    for point in cloud_array:
        projected_cloud_list.append(point - (normal*(np.dot(point,normal)/np.dot(normal,normal))))

    projected_cloud_array = np.array(projected_cloud_list, dtype=np.float32)
    return pcl.PointCloud(projected_cloud_array)