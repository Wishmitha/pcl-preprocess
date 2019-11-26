import numpy as np
import pcl

def pts_to_pcd(file, dest=None):

    filename = file.split('/')[-1].split('.')[0]

    if not dest:
        dest = ''.join(file.split('/')[:-1]) + filename + '.pcd'
    else:
        dest = dest + '/' + filename + '.pcd'

    lines = np.loadtxt(file)
    size = str(lines[:, 0].size)
    header = "VERSION .7\nFIELDS x y z\nSIZE 4 4 4\nTYPE F F F\nCOUNT 1 1 1\nWIDTH " + size + "\nHEIGHT 1\nVIEWPOINT 0 0 0 1 0 0 0\nPOINTS " + size + "\nDATA ascii"
    pcd = lines[:, [0, 1, 2]]
    np.savetxt(dest, pcd, fmt="%f", header=header, comments='')

def pcd_to_csv(file, dest=None):

    cloud = pcl.load(file)
    cloud_array = np.asarray(cloud)

    filename = file.split('/')[-1].split('.')[0]

    if not dest:
        dest = ''.join(file.split('/')[:-1]) + filename + '.csv'
    else:
        dest = dest + '/' + filename + '.csv'

    np.savetxt(dest, cloud_array, delimiter=",")

pcd_to_csv('/home/wolfpack/Dev/Datasets/Foot/pcd_data/sb1251ll.pcd','/home/wolfpack/Dev/Datasets/Foot/csv_data')
