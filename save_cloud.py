import pcl

def save(path=None, cloud=None): #visualize a pointcloud based on path or cloud

    pcl.save(cloud=cloud,path=path,format="pcd")
