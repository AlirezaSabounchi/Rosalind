import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})
lines,num_lines = [],0
with open("rosalind_pdst.txt") as file :
    text = file.read()
text = text.replace("\n", "").split(">")
for line in text :
    lines.append(line[14:])
    num_lines += 1
del lines[0]
num_lines -= 1
length = len(lines[1])
arr = np.zeros((num_lines,num_lines))
for i in range(0,num_lines):
    for j in range(0,num_lines):
        for k in range(0,length):
            if lines[i][k] != lines[j][k]:
                arr[i,j] += 1
arr /= length
print(str(arr).replace(' [', '').replace('[', '').replace(']', ''))
