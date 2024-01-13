name,content = [],[]
with open("rosalind_gc.txt") as file :
    lines = file.read()
lines = lines.replace("\n", "").split(">")
del lines[0]
for i in lines :
    name.append(i[0:13])
    content.append(100*(i[13:].count("C") + i[13:].count("G")) / (len(i)-13))
print(name[content.index(max(content))],max(content),sep="\n",end="")
