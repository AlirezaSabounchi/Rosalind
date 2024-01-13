def cost(letter1 , letter2):
    return scores[score_dic[letter1]][score_dic[letter2]]

################
with open('BLOSUM62.txt', 'r') as blosum:
    scores = [[int(score.rstrip()) for score in line.split(' ')] for line in blosum]
score_dic = {"A":0, "C":1,  "D":2,  "E":3,  "F":4,  "G":5,  "H":6,  "I":7,  "K":8,  "L":9,  "M":10,  "N":11,  "P":12,  "Q":13,  "R":14,  "S":15,  "T":16,  "V":17,  "W":18, "Y":19}

################################
import numpy as np
lines = []
with open("rosalind_gaff.txt") as file :
    text = file.read()
text = text.replace("\n", "").split(">")
for line in text :
    lines.append(line[13:])
del lines[0]

l1, l2 = len(lines[0]), len(lines[1])
arr , path = np.ones((3,l1+1,l2+1))*-999 , np.ones((l1+1,l2+1))
arr[0,:,0], arr[2,0,:] = range(-11,-12-l1,-1) , range(-11,-12-l2,-1)
arr[0,0,0] , arr[1,0,0] , arr[2,0,0] = -11 , -11 , 0
path[0,:], path[:,0], path[0,0] = 2,0,-1
##################

for i in range(1,l1+1) :
    for j in range(1,l2+1) :
        arr[0,i,j] = max(arr[0,i-1,j]-1 , arr[1,i-1,j]-11)
        arr[1,i,j] = max(arr[0,i-1,j-1] , arr[1,i-1,j-1] , arr[2,i-1,j-1]) + cost(lines[0][i-1],lines[1][j-1])
        arr[2,i,j] = max(arr[1,i,j-1]-11 , arr[2,i,j-1]-1)
        neighbors = [arr[0,i,j], arr[1,i,j], arr[2,i,j]]
        path[i,j] = neighbors.index(max(neighbors))
#################################
row, col = l1, l2
temp = [[], []]
while max(row,col)>0:
    if path[row, col] == 0 :
        temp[0].append(lines[0][row-1])
        temp[1].append("-")
        row -= 1
        continue
    if path[row, col] == 2 :
        temp[1].append(lines[1][col-1])
        temp[0].append("-")
        col -= 1
        continue
    if path[row, col] == 1 :
        temp[0].append(lines[0][row-1])
        temp[1].append(lines[1][col-1])
        row -= 1
        col -= 1
        continue
    break
print(int(arr[int(path[l1,l2]),l1,l2]))
[print(i, end="") for i in temp[0][::-1]]
print()
[print(i, end="") for i in temp[1][::-1]]
