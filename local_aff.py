import time as t
import numpy as np
start = t.time()

def blosum62():
    blosum_raw = """A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0 -2 -1  0 -4
    R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3 -1  0 -1 -4
    N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3  3  0 -1 -4
    D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3  4  1 -1 -4
    C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1 -3 -3 -2 -4
    Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2  0  3 -1 -4
    E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4
    G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3 -1 -2 -1 -4
    H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3  0  0 -1 -4
    I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3 -3 -3 -1 -4
    L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1 -4 -3 -1 -4
    K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2  0  1 -1 -4
    M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1 -3 -1 -1 -4
    F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1 -3 -3 -1 -4
    P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2 -2 -1 -2 -4
    S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2  0  0  0 -4
    T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0 -1 -1  0 -4
    W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3 -4 -3 -2 -4
    Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1 -3 -2 -1 -4
    V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4 -3 -2 -1 -4
    B -2 -1  3  4 -3  0  1 -1  0 -3 -4  0 -3 -3 -2  0 -1 -4 -3 -3  4  1 -1 -4
    Z -1  0  0  1 -3  3  4 -2  0 -3 -3  1 -1 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4
    X  0 -1 -1 -1 -2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -2  0  0 -2 -1 -1 -1 -1 -1 -4 """

    blosum_array1=[row.split(" ") for row in blosum_raw.split("\n")]

    blosum_array2= [[c for c in row if c!=""] for row in blosum_array1]

    blosum62 = {}
    blosum_entry_count = len(blosum_array2)
    for j in range(0, blosum_entry_count):
        for k in range(1,blosum_entry_count):
            row = blosum_array2[j]
            key = row[0] + blosum_array2[k-1][0]
            value = int(row[k])
            blosum62[key] = value
    return blosum62

blosum = blosum62()
lines, max_arr= [], []

with open("rosalind_gaff.txt") as file :
    text = file.read().replace("\n", "").split(">")
for line in text :
    lines.append(line[13:])
del lines[0]

l0, l1 = len(lines[0]), len(lines[1])
arr , path = np.zeros((3,l0+1,l1+1)) , np.ones((l0+1,l1+1))
arr[0,:,0], arr[2,0,:] = range(-11,-12-l0,-1) , range(-11,-12-l1,-1)
path[0,:], path[:,0], path[0,0] = 2, 0, 3
##################
for i in range(1,l0+1) :
    for j in range(1,l1+1) :
        arr[0,i,j] = max(arr[0,i-1,j]-1 , arr[1,i-1,j]-11, 0)
        arr[1,i,j] = max(arr[0,i-1,j-1] , arr[1,i-1,j-1] , arr[2,i-1,j-1], 0) + blosum["".join([lines[0][i-1],lines[1][j-1]])]
        arr[2,i,j] = max(arr[1,i,j-1]-11 , arr[2,i,j-1]-1, 0)
        path[i,j] = np.argmax(arr[:,i,j])
max = arr.max()
max_arr = np.argwhere(arr == max)
#################################
str0, str1 = max_arr[0][1], max_arr[0][2]
temp = [[0]*str0, [0]*str1]

while  arr[1 ,str0, str1]> 0 :
    if path[str0, str1] == 0:
        temp[0][str0-1] = lines[0][str0-1]
        str0 -= 1
        continue
    elif path[str0, str1] == 2 :
        temp[1][str1-1] = lines[1][str1-1]
        str1 -= 1
        continue
    elif path[str0, str1] == 1 :
        temp[0][str0-1] = lines[0][str0-1]
        temp[1][str1-1] = lines[1][str1-1]
        str0 -= 1
        str1 -= 1
        continue
print(int(max))
[print(i, end="") for i in temp[0]]
print()
[print(i, end="") for i in temp[1]]
end = t.time()
print()
print(end-start)
