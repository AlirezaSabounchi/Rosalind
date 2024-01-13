def base_conv(number , base , dic):
    new = []
    if number == 0:
        return ["A"]
    while number:
        new.append(dic.get(int(number % base)))
        number //= base
    return new[::-1]

with open("rosalind_lexf.txt") as file:
    letter = list(file.readline().rstrip().split())
    n = int(file.readline())
dict , l , base = {} , len(letter) , []
for i in letter :
    dict[letter.index(i)] = i
list = [str(i) for i in range(0,(l**n))]
for i in list :
    base.append("".join(base_conv(int(i),l,dict)))
    if len(base[list.index(i)]) < n :
        base[list.index(i)] = ((n - len(base[list.index(i)]))*"A") + base[list.index(i)]
[print(i) for i in base]
