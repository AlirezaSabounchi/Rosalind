def cost(index1 , index2 , same):
    if index1[0] == index2[0]-1 and index1[1] == index2[1]-1 and same:
        return 0
    else :
        return 1
################

import numpy as np
lines = []
with open("rosalind_edta.txt") as file :
    text = file.read()
text = text.replace("\n", "").split(">")
for line in text :
    lines.append(line[13:])
del lines[0]
l1, l2 = len(lines[0]), len(lines[1])
arr , path = np.zeros((l1+1,l2+1)) , np.ones((l1+1,l2+1))
arr[0,:], arr[:,0], arr[0][0] = 1 , 1 , 0
path[0,:], path[:,0], path[0,0] = 2, 1, 9
##################

for i in range(1,l1+1) :
    for j in range(1,l2+1) :
        if lines[0][i-1] == lines[1][j-1] :
            same = 1
        else :
            same = 0
        from_index = [1,2,3]
        neighbors = [arr[i-1,j]+cost([i-1,j],[i,j],same),arr[i,j-1]+cost([i,j-1],[i,j],same),arr[i-1,j-1]+cost([i-1,j-1],[i,j],same)]
        arr[i,j] = min(neighbors)
        path[i,j] = (from_index[neighbors.index(min(neighbors))])
#################################
row, col = l1, l2
temp = [[], []]
while min(row,col)>0:
    if path[row, col] == 1 :
        temp[0].append(lines[0][row-1])
        temp[1].append("-")
        row -= 1
        continue
    elif path[row, col] == 2 :
        temp[1].append(lines[1][col-1])
        temp[0].append("-")
        col -= 1
        continue
    elif path[row, col] == 3 :
        temp[0].append(lines[0][row-1])
        temp[1].append(lines[1][col-1])
        row -= 1
        col -= 1
        continue
print(int(arr[l1,l2]))
[print(i, end='') for i in temp[0][::-1]]
print()
[print(i, end='') for i in temp[1][::-1]]
