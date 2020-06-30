import random
import numpy as np
import math


def replace_line(lines, file_name, line_num, text):
    # print(lines)
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

for i in range(1,55):
    file_name_read = '../../Datasets/Foot/off_data/sam_'+str(i)+'.off'
    file_name_write = '../../Datasets/Foot/off_data/mod/sam_'+str(i)+'_mod.off'
    off = open(file_name_read,'r+')
    lines = off.readlines()
    num = 1
    mod=[]
    for line in lines:
        if len(line.split())==3 and num > 2 and num < 2000:
            vertices = []
            vert = line.split();
            for val in vert:
                val = float(val) + random.randint(-8,8)
                #val = 'lol'
                vertices.append(str(int(val)))
            mod.append([vertices,num])
        num += 1

    #print(mod)

    for lin in mod:
        #print(lin[-1]," ".join(lin[0]))
        replace_line(lines,file_name_write,lin[-1]," ".join(lin[0])+'\n')


    off.close()