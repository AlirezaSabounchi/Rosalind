def UPGMA(dist_mtx, n):
    #start = t.time()
    cluster, adjucency, age = [],[],[]
    D = np.array(dist_mtx, dtype = float)

    for i in range(n) :
        D[i,i] = np.inf
        #cluster = [nodes, length]
        cluster.append([i, 1])
        adjucency.append([])
        age.append([0.])

    while len(D) > 1:
        #index of min distances with min i
        index = np.argmin(D)
        i = index // len(D)
        j = index % len(D)
        #determin age for new cluster
        age.append(D[i, j] / 2)
        #add a new row at the end of adjacency
        i_cluster = len(adjucency)
        #add new cluster to adjacency
        adjucency.append([])
        adjucency[i_cluster].append(cluster[i][0])
        adjucency[i_cluster].append(cluster[j][0])
        adjucency[cluster[i][0]].append(i_cluster)
        adjucency[cluster[j][0]].append(i_cluster)
        #create cluster_new and calculate length
        cluster_new = [i_cluster, cluster[i][1] + cluster[j][1]]
        cluster.append(cluster_new)
        #new d value for cluster(i,j)
        d_new = (D[i,:]*cluster[i][1] + D[j,:]*cluster[j][1]) / (cluster[i][1] + cluster[j][1])
        #print(d_new)
        d_new = np.delete(d_new, [i, j])
        #print(d_new)
        #delete row an col i j from D
        D = np.delete(D, [i, j], 0)
        D = np.delete(D, [i, j], 1)
        #print(D)
        #insert cluster in D
        D = np.insert(D, len(D), d_new, axis = 0)
        #print(D)
        D = np.insert(D, len(D)-1, np.insert(d_new, len(d_new), np.inf, axis = 0), axis = 1)
        #print(D)

        del cluster[max(i,j)], cluster[min(i,j)]

    adj_list = adjucency
    for v, nodes in enumerate(adjucency):
        for j, w in enumerate(nodes):
            adj_list[v][j] = (w, abs(age[v]-age[w]))
    #end = t.time()
    #print(end-start)
    return adj_list

############################
import time as t
import numpy as np

temp = []
with open("rosalind_ba7d.txt") as file :
    for line in file:
        temp.append(line.strip())

n = int(temp[0])
dist_mtx = np.zeros((n,n))

for row in range(n):
    a = temp[row+1].split()
    for col in range(n):
        dist_mtx[row][col] = int(a[col])

#show list as formatted line
adj_list = UPGMA(dist_mtx, n)
for i, nodes in enumerate(adj_list):
    for d, w in nodes:
        print(str(i)+'->'+str(d)+':'+'%0.3f' % w)
