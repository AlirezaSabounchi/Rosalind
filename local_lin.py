
with open('PAM250.txt', 'r') as PAM:
    scores = [[int(score.rstrip()) for score in line.split(' ')] for line in PAM]
score_dic = {"A":0, "C":1,  "D":2,  "E":3,  "F":4,  "G":5,  "H":6,  "I":7,  "K":8,  "L":9,  "M":10,  "N":11,  "P":12,  "Q":13,  "R":14,  "S":15,  "T":16,  "V":17,  "W":18, "Y":19}

################################
import numpy as np
lines, max_arr = [],[[-999],[]]

with open("rosalind_loca.txt") as file :
    text = file.read()
text = text.replace("\n", "").split(">")
for line in text :
    lines.append(line[13:])
del lines[0]
l0, l1 = len(lines[0]), len(lines[1])
arr , path = np.zeros((l0+1,l1+1)) , np.ones((l0+1,l1+1))*3
arr[0,:], arr[:,0], arr[0][0] = -5 , -5 , 0
path[0,:], path[:,0], path[0,0] = 2, 0, 3
##################
for i in range(1,l0+1) :
    for j in range(1,l1+1) :
        neighbors = [arr[i-1,j]-5, arr[i-1,j-1] + scores[score_dic[lines[0][i-1]]][score_dic[lines[1][j-1]]], arr[i,j-1]-5, 0]
        arr[i,j] = max(neighbors)
        path[i,j] = neighbors.index(arr[i,j])
        if max_arr[0] <= arr[i,j] :
            max_arr[0] = int(arr[i,j])
            max_arr[1] = [i,j]
#################################
str0, str1 = max_arr[1][0], max_arr[1][1]
temp = [[], []]
while  arr[str0, str1]> 0:
    if path[str0, str1] == 0:
        temp[0].append(lines[0][str0-1])
        temp[1].append("")
        str0 -= 1
        continue
    elif path[str0, str1] == 2 :
        temp[1].append(lines[1][str1-1])
        temp[0].append("")
        str1 -= 1
        continue
    elif path[str0, str1] == 1 :
        temp[0].append(lines[0][str0-1])
        temp[1].append(lines[1][str1-1])
        str0 -= 1
        str1 -= 1
        continue
    elif path[str0,str1] == 3 :
        break
print(int(max_arr[0]))
[print(i, end="") for i in temp[0][::-1]]
print()
[print(i, end="") for i in temp[1][::-1]]
