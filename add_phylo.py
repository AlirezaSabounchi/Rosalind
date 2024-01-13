#limbLength func
def limb_length(dist_mtx, n, j) :
    limbLength = float('inf')

    if j == 0 :
        i = 1
    else :
        i = j-1

    for k in range(n) :
        if i!=k and k!=j :
                temp = (dist_mtx[i][j] + dist_mtx[j][k] - dist_mtx[i][k])//2
                if temp < limbLength :
                    limbLength = temp
                    indx = [i,k]
    return int(limbLength), indx[0], indx[1]

# phylogeny func
def phylogeny(dist_mtx, n):
    adjacency = [dict() for i in range(n)]
    adjacency[0][1], adjacency[1][0] = dist_mtx[0][1], dist_mtx[1][0]

    for j in range(2, n):
        limbLength, i, k = limb_length(dist_mtx, j+1, j)
        x = dist_mtx[i][j] - limbLength
        adjacency = add_node(adjacency, limbLength, i, j, k, x)
    return adjacency

#AddNode func
def add_node(adjacency, limbLength, i, j, k, x):
    l = len(adjacency)
    dist, parent, dist[i] = [float('inf')] * l, [-1] * l, 0
    q = queue.Queue()
    q.put(i)

    start = t.time()
    while q:
        curr = q.get()
        for node, weight in adjacency[curr].items():
            if float('inf') == dist[node]:
                parent[node] = curr
                dist[node] = dist[curr] + weight

                q.put(node)
                if node == k:
                    prev = node
                    while x < dist[prev]:
                        curr = prev
                        prev = parent[curr]
                    # is node at distance x from
                    if x == dist[prev]:
                        adjacency[j][prev], adjacency[prev][j] = limbLength, limbLength

                    else:
                        # reduce matrix dimention
                        del adjacency[prev][curr], adjacency[curr][prev]

                        adjacency.append(dict())
                        #index of the new node
                        new = len(adjacency) - 1
                        #replacing former values
                        adjacency[new][prev], adjacency[prev][new] = x-dist[prev], x-dist[prev]
                        adjacency[new][curr], adjacency[curr][new] = dist[curr]-x, dist[curr]-x
                        adjacency[new][j], adjacency[j][new] = limbLength, limbLength

                    end = t.time()
                    #print(end-start)

                    return adjacency
##################################
import time as t
import numpy as np
import queue

temp = []
with open("rosalind_ba7c.txt") as file :
    for line in file:
        temp.append(line.strip())

n = int(temp[0])
dist_mtx = np.zeros((n,n))

for row in range(n):
    a = temp[row+1].split()
    for col in range(n):
        dist_mtx[row][col] = int(a[col])

#print graph
adj_list = phylogeny(dist_mtx, n)
for i, dicts in enumerate(adj_list):
    for d, w in dicts.items():
        print(str(i)+'->'+str(d)+':'+str(int(w)))
