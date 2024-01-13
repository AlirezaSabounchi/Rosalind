def limb_length(dist_mtx, n, j) :
    length = float('inf')

    if j == 0 :
        i = j+1
    else :
        i = j-1
    for k in range(n) :
        if i!=k and k!=j :
                temp = (dist_mtx[i][j] + dist_mtx[j][k] - dist_mtx[i][k])//2
                if temp < length :
                    length = temp
    return int(length)

################
import numpy as np
import time as t
#start = t.time()
with open("rosalind_ba7b.txt") as file :
    num_leaves = int(file.readline())
    leaf = int(file.readline())
    dist_mtx = np.zeros((num_leaves,num_leaves))

    for row in range(num_leaves) :
        temp = file.readline().split()
        #print(temp)
        for col in range(num_leaves) :
            dist_mtx [row][col] = int(temp[col])
#print(dist_mtx)
print(limb_length(dist_mtx, num_leaves, leaf))
#end = t.time()
#print(end-start)
