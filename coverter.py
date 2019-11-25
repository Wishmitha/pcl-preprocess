from numpy import loadtxt
from numpy import savetxt

def pts_to_pcd(file, dest=None):

    filename = file.split('/')[-1].split('.')[0]

    if not dest:
        dest = ''.join(file.split('/')[:-1]) + filename + '.pcd'
    else:
        dest = dest + '/' + filename + '.pcd'

    lines = loadtxt(file)
    size = str(lines[:, 0].size)
    header = "VERSION .7\nFIELDS x y z\nSIZE 4 4 4\nTYPE F F F\nCOUNT 1 1 1\nWIDTH " + size + "\nHEIGHT 1\nVIEWPOINT 0 0 0 1 0 0 0\nPOINTS " + size + "\nDATA ascii"
    pcd = lines[:, [0, 1, 2]]
    savetxt(dest, pcd, fmt="%f", header=header, comments='')

#pts_to_pcd('/home/wolfpack/Dev/Datasets/Foot/pts_data/sb1251ll.pts', '/home/wolfpack/Dev/Datasets/Foot/pcd_data')