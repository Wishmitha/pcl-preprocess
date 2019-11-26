from visualizer import visualize
from planar__projection import project

import pcl

cloud = pcl.load('/home/wolfpack/Dev/Datasets/Foot/pcd_data/sb1251ll.pcd')

pro_cloud = project(cloud, [0,0,1,0])

visualize(cloud=pro_cloud)