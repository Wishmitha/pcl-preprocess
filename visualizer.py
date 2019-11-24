import pcl
import pcl.pcl_visualization


def visualize(path=None, cloud=None): #visualize a pointcloud based on path or cloud

    viewer = pcl.pcl_visualization.PCLVisualizering()

    if not cloud:

        cloud = pcl.load(path)

        while(True):
            viewer.AddPointCloud(cloud, b'scene_cloud', 0)
            viewer.SpinOnce()
            viewer.RemovePointCloud(b'scene_cloud', 0)
    else:

        while (True):
            viewer.AddPointCloud(cloud, b'scene_cloud', 0)
            viewer.SpinOnce()
            viewer.RemovePointCloud(b'scene_cloud', 0)

