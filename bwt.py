from copy import deepcopy

with open("rosalind_ba9j.txt") as file :
    data = file.read().strip()
bwt_col = [[i] for i in data]
[bwt_col[i].append(data[:i+1].count(bwt_col[i][0])) for i in range(len(data))]
first = sorted(deepcopy(bwt_col), key = lambda l: l[0])
ind, temp = 0, []

for char in range(len(bwt_col)) :
    temp.append(bwt_col[ind][0])
    ind = bwt_col.index(first[ind])

temp = ''.join(temp)
print(temp[temp.index('$')+1:] + temp[:temp.index('$')] + '$')
