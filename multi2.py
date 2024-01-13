import numpy as np
def align(str0, str1) :
    def cost(letter1, letter2, letter3, letter4):
        if letter1 == letter2 and letter:
            return 0
        else :
            return -1

    #   #   #   #   #   #   #   #   #

    l0, l1, l2, l3 = len(str0), len(str1), len(str2), len(str3)
    arr = np.zeros((l0+1,l1+1,l2+1,l3+1))
    arr[0,:], arr[:,0] = range(0,-l1-1,-1) , range(0,-l0-1,-1)
    path = []

    #   #   #   #   #   #   #   #   #

    for i in range(1,l0+1) :
        for j in range(1,l1+1) :
            for k in range(1,l2+1) :
                for l in range(1,l3+1)
                    neighbors = [ arr[i-1,j-1] + cost(str0[i-1], str1[j-1], str2[k-1], str3[l-1])]
            arr[i,j] = max(neighbors)
    path[i,j] = neighbors.index(arr[i,j])

    #   #   #   #   #   #   #   #   #
    final = []
    row, col = l0, l1
    temp = [[], []]
    while row or col :
        if path[row, col] == 0 :
            temp[0].append(str0[row-1])
            temp[1].append("-")
            row -= 1
            continue
        elif path[row, col] == 2 :
            temp[1].append(str1[col-1])
            temp[0].append("-")
            col -= 1
            continue
        elif path[row, col] == 1 :
            temp[0].append(str0[row-1])
            temp[1].append(str1[col-1])
            row -= 1
            col -= 1
            continue
    for i in range(len(temp[0])):
        if temp[0][i] == temp[1][i] or temp[0][i] != temp[1][i] :
            final.append(temp[0][i])
        elif temp[0][i] == "-" or temp[1][i] == "-" :
            final.append(max(temp[0][i], temp[1][i]))
        result = final[::-1]
        f = temp[0][::-1]
        s = temp[1][::-1]
    return [int(arr[l0,l1]), result, f, s]

str, strings = [],[]
with open("rosalind_mult.txt") as file :
    text = file.read()
text = text.replace("\n", "").split(">")
for line in text :
    str.append(line[13:])
    strings.append(line[13:])
del str[0], strings[0]

num = len(str)
arr = np.ones((num,num))*-999
result, maxim = [], [0]*2

for k in range(0,3) :
    for i in range(0, num-1) :
        for j in range(i+1, num) :
            result.append(align(str[i], str[j]))
            arr[i,j], arr[j,i] = result[j-1][0], result[j-1][0]
    maxim[0], maxim[1] = (np.argmax(arr) // (num+1)), (np.argmax(arr) % (num+1))
    str[maxim[0]] = "".join(result[maxim[1]-1][1])
    del str[maxim[1]]
#    print(arr.max())
    num -= 1
    result = []
    arr = np.ones((num,num))*-999
    if k == 2 :
        source = str[0]
aligned, final_sc = [], 0

[aligned.append("".join(align(source, strings[i])[3])) for i in range(len(strings))  ]
ar = np.zeros((4,4))
for i in range(len(aligned[0])) :
    for j in range(4) :
        for k in range(4) :
            if aligned[j][i] != aligned[k][i] :
                ar[j,k] = -1
            else :
                ar[j,k] = 0
    final_sc += np.sum(ar)/2
print(int(final_sc))
[print("".join(align(source, strings[i])[3])) for i in range(len(strings))]
