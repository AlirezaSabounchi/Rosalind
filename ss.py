from itertools import*
import functools as fun
def rev_comp(input) :
    dict, result = {"A":"T" , "T":"A" , "C":"G" , "G":"C"}, []
    for letter in reversed(input) :
        result.append(dict[letter])
    result = "".join(result)
    return result

with open("temp.txt") as file :
    text = file.read().split("\n")
data = []
for line in text :
    data.append(line)
    data.append(rev_comp(line))

print(data)
print(min((fun.reduce(lambda s,w:(w+s[max(i*(s[:i]==w[-i:])for i in range(len(data[0]))):],s)[w in s],p)
for p in permutations(data)),key=len))
