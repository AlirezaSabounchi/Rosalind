def small_pars(n, children, parent, adj, nodes, char2ind, ind2char, ind_char):
    processed, ripe, score = [], set(), []
    backtrack = [[[0, 0] for j in range(4)] for i in range(len(children))]
    #initial score = inf
    for i in range(len(children)) :
        processed.append(False)
        score.append([np.inf]*4)
    #if node = char(leaf) then score = 0
    for i in range(n):
        score[i][char2ind[nodes[i][ind_char]]] = 0
        processed[i] = True
        if len(parent[i]) > 0:
            ripe.add(parent[i][0])
    #get a parent with processed children
    while ripe :
        v = ripe.pop()
        #set score as min(children) and record for backtrack
        for k in range(4):
            left_child = [score[children[v][0]][i] + (int(k!=i)) for i in range(4)]
            right_child = [score[children[v][1]][i] + (int(k!=i)) for i in range(4)]
            #print(left_child,right_child)
            #cal min child
            min_left = np.argmin(left_child)
            min_right = np.argmin(right_child)
            backtrack[v][k] = (min_left, min_right)
            score[v][k] = left_child[min_left] + right_child[min_right]
        processed[v] = True
        #if all children processed = ripe
        if parent[v] and all([processed[i] for i in children[parent[v][0]]]):
            ripe.add(parent[v][0])

    min_ind = np.argmin(score[v])
    nodes[v] += ind2char[min_ind]
    #print(nodes)
    min_score = score[v][min_ind]

    #backtrace from root using BFS
    bfs_queue = queue.Queue()
    bfs_queue.put((v, min_ind))

    while not bfs_queue.empty():
        v, k = bfs_queue.get()
        if len(children[v]) > 0:
            u, w = children[v]
            left_child, right_child = backtrack[v][k]

            if k != left_child:
                adj[v][u] += 1
                adj[u][v] += 1
            if k != right_child:
                adj[v][w] += 1
                adj[w][v] += 1
            if len(children[u]) > 0:
                nodes[u] += ind2char[left_child]
                nodes[w] += ind2char[right_child]
                bfs_queue.put((u, left_child))
                bfs_queue.put((w, right_child))
    #print(left_child, right_child)
    return min_score

########
import queue
import numpy as np
import time as t
#start = t.time()
children, parent, adj, nodes, current = [], [], [], [], 0
#read file
with open("rosalind_ba7f.txt") as file :
    data = file.read().strip().split('\n')
    n = int(data[0])
#initiate variables
    for i in range(n) :
        children.append([])
        parent.append([])
        adj.append(dict())
        nodes.append('')
#reformat ugly input to something readable
    for line in data[1:] :
        line = line.split('->')
        from_node = int(line[0])
        #if to is int
        try:
            to_node = int(line[1])
        #if to is str
        except:
            to_node = current
            nodes[to_node] = line[1]
            current += 1
        #extend lists cause we dont know how many nodes we have /:
        if from_node > len(children)-1 or to_node > len(children)-1 :
            for i in range(max([from_node,to_node])-len(children)+1) :
                children.append([])
            for i in range(max([from_node,to_node])-len(parent)+1) :
                parent.append([])
            for i in range(max([from_node,to_node])-len(adj)+1) :
                adj.append(dict())
        #add child/parent
        children[from_node].append(to_node)
        parent[to_node].append(from_node)
        adj[from_node][to_node] = 0
        adj[to_node][from_node] = 0
    for i in range(len(children)-n) :
        nodes.append('')
#print(n, children, parent, adj, nodes)

char2ind, ind2char = {'A':0, 'C':1, 'G':2, 'T':3}, {0:'A', 1:'C', 2:'G', 3:'T'}
score = 0
for i in range(len(nodes[0])):
    score += small_pars(n, children, parent, adj, nodes, char2ind, ind2char, i)
#end = t.time()
#print(end-start)

#print in format
print(score)
for s, d in enumerate(adj):
    for j, w in d.items():
        print(nodes[s]+'->'+nodes[j]+':'+str(w))
