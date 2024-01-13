from copy import deepcopy
import numpy as np
import time as t

lexicon = ['$', 'A', 'C', 'G', 'T']
char_count, char_start = dict(), dict()

#bwt_col = [[i] for i in data]
#[bwt_col[i].append(data[:i+1].count(bwt_col[i][0])) for i in range(len(data))]
#first = sorted(deepcopy(bwt_col), key = lambda l: l[0])
ind, reference = 0, []

with open("rosalind_ba9l.txt") as file :
    bwt = file.readline().strip()
    patterns = file.readline().strip().split()
len_btw = len(bwt)

for char in lexicon:
    char_count[char] = [0] * (len_btw + 1)
for i in range(len_btw):
    cur_char = bwt[i]
    for char, count in char_count.items():
        char_count[char][i+1] = char_count[char][i]
    char_count[cur_char][i+1] += 1

cur_indx = 0
for char in lexicon:
    char_start[char] = cur_indx
    cur_indx += char_count[char][len_btw]
#print(char_count, char_start)
occur_char_count = []
#start = t.time()
for query in patterns:
    cur_indx = len(query) - 1
    top = 0
    bottom = len(bwt) - 1
    while top <= bottom:
        if cur_indx >= 0:
            cur_char = query[cur_indx]
            cur_indx -= 1
            if char_count[cur_char][bottom + 1] - char_count[cur_char][top] > 0:
                top = char_start[cur_char] + char_count[cur_char][top]
                bottom = char_start[cur_char] + char_count[cur_char][bottom + 1] - 1
            else:
                occur_char_count.append(0)
                break
        else:
            occur_char_count.append(bottom - top + 1)
            break
        #print(occur_char_count)
    #occur_char_count.append(bottom - top+!)
#end=t.time()
#print(end - start)
[print(occur_char_count[i], end=' ') for i in range(len(occur_char_count))]
