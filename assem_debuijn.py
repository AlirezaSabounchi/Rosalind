import time as t
begin = t.time()

def rev_comp(input) :
    dict, result = {"A":"T" , "T":"A" , "C":"G" , "G":"C"}, []
    for letter in reversed(input) :
        result.append(dict[letter])
    result = "".join(result)
    return result

def is_next(string, head, data, k) :
    for word in data :
        if word.startswith(head[k:]) and word not in string :
            return True, word
    return False, []

def construct(list, k) :
    result = []
    result.append(list[0])
    for i in list[1:] :
        result.append(i[k:])
    return "".join(result)

def de_bruijn(kplus1, k) :
    edges = []
    for kmer in kplus1 :
        edges.append(kmer[0:k-1])
        edges.append(kmer[1:k])
        #nodes.add(kmer[0:k-1])
        #nodes.add(kmer[1:k])
    return edges

with open("temp.txt") as file :
    text = file.read().split("\n")

data = []
for line in text :
    data.append(line)
    data.append(rev_comp(line))

edges = de_bruijn(data,len(data[0]))

temp, string = [], []
for k in range(1,len(edges[0])) :
    start = edges[0]
    while 1 :
        next_found, next = is_next(string, start, edges, k)
        if next_found:
            string.append(next)
            start = next
            continue
        else :
            break
    print(len(string))
    if len(string) == len(text) :
        #ignore = len(edges[0]) // k
        #print(string)
        #for i in range(ignore-1):
        #    del string[-1]
        #print(string)
        temp = construct(string, k)
        break
    string = [edges[0]]

ending = t.time()
print(temp[:len(temp)], k)

#-ignore*(len(data[0])-k)
#print(construct(max(string, key=len)))
#print(construct(string[string.index(max(string, key=len))]))
