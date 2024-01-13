def neighbor_join(dist_mtx, n):
    adjacency, clusters = [], []
    D = np.array(dist_mtx, dtype = float)

    for i in range(n) :
        adjacency.append([])
        clusters.append(i)

    while 1 :
        #tree consisting of a single edge
        if n == 2:
            adjacency[len(adjacency)-1].append((len(adjacency)-2, D[0][1]))
            adjacency[len(adjacency)-2].append((len(adjacency)-1, D[1][0]))
            return adjacency
        #sum rows as a column
        TotalDistance = np.sum(D, axis = 0)
        D1 = ((n-2) * D) - 2 * TotalDistance
        D1 = D1 - TotalDistance.reshape((n, 1))
        # D1 as D prime
        for i in range(len(D1)) :
            D1[i,i] = 0.
        #find arg of min dist
        index = np.argmin(D1)
        i = index // n
        j = index % n
        #delta = sum of dist i-j by n-2
        delta = (TotalDistance[i] - TotalDistance[j]) / (n-2)
        limbLength_i = (D[i, j] + delta) / 2
        limbLength_j = (D[j, i] - delta) / 2
        #add a new row/column m to D so that Dk,m = Dm,k = (1/2)(Dk,i + Dk,j - Di,j) for any k
        d_new = (D[i, :] + D[j, :] - D[i, j]) / 2
        D = np.insert(D, n, d_new, axis = 0)
        d_new = np.insert(d_new, n, 0., axis = 0)
        D = np.insert(D, n, d_new, axis = 1)
        #remove rows i and j from D
        D = np.delete(D, [i, j], 0)
        #remove columns i and j from D
        D = np.delete(D, [i, j], 1)
        n -= 1

        #add two new limbs (connecting node m with leaves i and j) to the tree T
        m = len(adjacency)
        adjacency.append([])
        adjacency[m].append((clusters[i], limbLength_i))
        adjacency[m].append((clusters[j], limbLength_j))
        adjacency[clusters[i]].append((m, limbLength_i))
        adjacency[clusters[j]].append((m, limbLength_j))
        clusters.append(m)
        #delete cluster i,j from clusters
        del clusters[max(i,j)], clusters[min(i,j)]

    return adjacency

#####################
import time as t
import numpy as np

temp = []
with open("rosalind_ba7e.txt") as file :
    for line in file:
        temp.append(line.strip())

n = int(temp[0])
dist_mtx = np.zeros((n,n))

for row in range(n):
    a = temp[row+1].split()
    for col in range(n):
        dist_mtx[row][col] = int(a[col])

#print graph
adj_list = neighbor_join(dist_mtx, n)
for i, nodes in enumerate(adj_list):
    for d, w in nodes:
        print(str(i)+'->'+str(d)+':'+'%0.3f' % w)
