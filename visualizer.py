import pcl
import pcl.pcl_visualization


def visualize(path=None, cloud=None): #visualize a pointcloud based on path or cloud

    viewer = pcl.pcl_visualization.PCLVisualizering()

    if not cloud:

        cloud = pcl.load(path)

        while(True):
            viewer.AddPointCloud(cloud, b'cloud', 0)
            viewer.SpinOnce()
            viewer.RemovePointCloud(b'cloud', 0)
    else:

        while (True):
            viewer.AddPointCloud(cloud, b'cloud',0)
            viewer.SpinOnce()
            viewer.RemovePointCloud(b'cloud',0)

def multi_visualize(clouds=[], paths=[]):

    viewer = pcl.pcl_visualization.PCLVisualizering()

    cloud_list = []

    for path in paths:
        cloud_list.append(pcl.load(path))

    for cloud in clouds:
        cloud_list.append(cloud)

    id = 0

    for cloud in cloud_list:
        id_str = bytes('cloud' + str(id), encoding='utf8')
        viewer.AddPointCloud(cloud, id_str, id)
        id = id + 1

    while (True):
        viewer.SpinOnce()






