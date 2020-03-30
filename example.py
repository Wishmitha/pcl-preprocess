from visualizer import visualize
from planar__projection import project
from  generator import generate
from  generator import rnd_generate
from generator import pro_generate
from save_cloud import save


import pcl

cloud = pcl.load('/home/wolfpack/Dev/Datasets/Foot/pcd_data/sb1253ll.pcd')
visualize(cloud=cloud)

pro_cloud = project(cloud, [1,1,1,0])
#visualize(cloud=pro_cloud)
#save(cloud=pro_cloud, path="test.pcd")

#gen_cloud = generate(cloud)
#visualize(cloud=gen_cloud)

gen_cloud = rnd_generate(cloud)
visualize(cloud=gen_cloud)
save(cloud=gen_cloud, path="test.pcd")

#pro_gen_cloud = pro_generate(cloud)
#visualize(cloud=pro_gen_cloud)
#save(cloud=pro_gen_cloud, path="test.pcd")