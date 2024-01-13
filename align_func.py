import numpy as np
def align(self, str0, str1) :
    def cost(letter1 , letter2):
        if letter1 == letter2 :
            return 0
        else :
            return -1

    #   #   #   #   #   #   #   #   #

    l0, l1 = len(str0), len(str1)
    arr , path = np.zeros((l0+1,l1+1)) , np.ones((l0+1,l1+1))
    arr[0,:], arr[:,0] = range(0,-l1-1,-1) , range(0,-l0-1,-1)
    path[0,:], path[:,0], path[0,0] = 2, 0, 3

    #   #   #   #   #   #   #   #   #

    for i in range(1,l0+1) :
        for j in range(1,l1+1) :
            neighbors = [arr[i-1,j]-1, arr[i-1,j-1]+cost(lines[0][i-1],lines[1][j-1]), arr[i,j-1]-1]
            arr[i,j] = max(neighbors)
            path[i,j] = neighbors.index(arr[i,j])

    #   #   #   #   #   #   #   #   #

    row, col = l0, l1
    temp = [[], []]
    while row or col :
        if path[row, col] == 0 :
            temp[0].append(lines[0][row-1])
            temp[1].append("-")
            row -= 1
            continue
        elif path[row, col] == 2 :
            temp[1].append(lines[1][col-1])
            temp[0].append("-")
            col -= 1
            continue
        elif path[row, col] == 1 :
            temp[0].append(lines[0][row-1])
            temp[1].append(lines[1][col-1])
            row -= 1
            col -= 1
            continue
    return([int(arr[l0,l1]), temp])
