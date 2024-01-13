def rev_comp(input) :
    dict, result = {"A":"T" , "T":"A" , "C":"G" , "G":"C"}, []
    for letter in reversed(input) :
        result.append(dict[letter])
    result = "".join(result)
    return result

def de_bruijn(kplus1, k) :
    edges, nodes = [], set()
    for kmer in kplus1 :
        edges.append(", ".join((kmer[0:k-1], kmer[1:k])))
        nodes.add(kmer[0:k-1])
        nodes.add(kmer[1:k])
    return nodes, edges

with open("rosalind_dbru.txt") as file :
    text = file.read().split("\n")

data = set()
for line in text :
    data.add(line)
    data.add(rev_comp(line))

nodes, edges = de_bruijn(data,50)
edges.sort()

[print("(", edge, ")", sep="", end="\n") for edge in edges]
