from copy import deepcopy
import numpy as np

with open("temp.txt") as file :
    data = file.readline().strip()
    patterns = file.readline().strip().split(' ')
#print(data,patterns, sep='\n')
bwt_col = [[i] for i in data]
[bwt_col[i].append(data[:i+1].count(bwt_col[i][0])) for i in range(len(data))]
first = sorted(deepcopy(bwt_col), key = lambda l: l[0])
ind, reference = 0, []

for char in range(len(bwt_col)) :
    reference.append(bwt_col[ind][0])
    ind = bwt_col.index(first[ind])

reference = ''.join(reference[reference.index('$')+1:] + reference[:reference.index('$')] + ['$'])
len_ref = len(reference)
bwt_mtrx = [[] for _ in range(len_ref)]

for i in range(len_ref) :
    for j in range(len_ref) :
        if j+i > len_ref-1 :
            bwt_mtrx[i].append(reference[(j+i)%len_ref])
        else :
            bwt_mtrx[i].append(reference[j+i])
bwt_mtrx = sorted(bwt_mtrx, key= lambda l : l[:])

print()
