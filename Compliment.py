dna = open("rosalind_revc.txt" , "r").readline()
temp = []
for i in dna :
    if i == "A" :
        temp.append("T")
    if i == "C" :
        temp.append("G")
    if i == "T" :
        temp.append("A")
    if i == "G" :
        temp.append("C")
[print(i,end="") for i in temp[::-1]]
