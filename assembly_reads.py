def rev_comp(input) :
    dict, result = {"A":"T" , "T":"A" , "C":"G" , "G":"C"}, []
    for letter in reversed(input) :
        result.append(dict[letter])
    result = "".join(result)
    return result
def is_next(head, data, k) :
    for word in data :
        if word.startswith(head[k:]) :
            if data.index(word) > 1 :
                if data[data.index(word)-1] == rev_comp(word) :
                    del data[data.index(word)-1:data.index(word)+1]
                else :
                    del data[data.index(word):data.index(word)+2]
                return True, word, data
            elif data.index(word) == 0 or data.index(word) == 1  :
                del data[0:2]
                return True, word, data
    return False, [], data

def construct(list, k) :
    result = []
    result.append(list[0])
    for i in list[1:] :
        result.append(i[k:])
    return "".join(result)

def superstring(dna_strings):
    for kval in range(1, len(dna_strings[0])):
        edges_set = set()
        for kmer in dna_strings:
            for i in range(kval):
                edges_set.add(kmer[i : i + len(kmer) - kval + 1])
                edges_set.add(rev_comp(kmer[i : i + len(kmer) - kval + 1]))
        k = len(list(edges_set)[0])
        graph_edges = [[each_edge[0:k - 1], each_edge[1:k]] for each_edge in edges_set]
        ###### identify cyclic superstring and check if set gets empty
        superstring_cycle = []
        for i in range(2):
            pop_kmer = graph_edges.pop(0)
            cycle = pop_kmer[0][-1]
            while pop_kmer[1] in [each[0] for each in graph_edges]:
                ######## add characters in string NOT LIST!!!!!
                cycle += pop_kmer[1][-1]
                index = []
                for i,edge in enumerate(graph_edges):
                    if edge[0] == pop_kmer[1]:
                        index.append(i)
                pop_kmer = graph_edges.pop(index[0])
            superstring_cycle.append(cycle)

        if not len(graph_edges):
            break
    return superstring_cycle

################
with open("rosalind_gasm.txt") as file :
    text = file.read().split("\n")
    del text[-1]

    result1, result2 = superstring(text)
    print(result1)
