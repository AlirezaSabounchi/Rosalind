import numpy as np
import queue
class SmallParsimony:
    def __init__(self):
        n, adjC, adjP, adj, nodes = self._input()
        s = self.runSmallParsimony(n, adjC, adjP, adj, nodes)
        self.printResults(s, adj, nodes)


    def _input(self):
        file = open("temp.txt", "r")
        data = file.read().strip().split('\n')
        n = int(data[0])
        adjC = [[] for _ in range(n)]
        adjP = [[] for _ in range(n)]
        adj = [dict() for _ in range(n)]
        nodes = ['' for _ in range(n)]
        currNode = 0
        for d in data[1:]:
            d = d.split('->')
            p = int(d[0])
            try:
                c = int(d[1])
            except:
                c = currNode
                nodes[c] = d[1]
                currNode += 1
            if p > len(adjC)-1 or c > len(adjC)-1:
                adjC.extend([[] for _ in range(max([p,c])-len(adjC)+1)])
                adjP.extend([[] for _ in range(max([p,c])-len(adjP)+1)])
                adj.extend([dict() for _ in range(max([p,c])-len(adj)+1)])
            adjC[p].append(c)
            adjP[c].append(p)
            adj[p][c] = 0
            adj[c][p] = 0
        nodes.extend(['' for _ in range(len(adjC)-n)])
        print(adjC, adjP, adj, nodes)
        return n, adjC, adjP, adj, nodes

    def printResults(self, s, adj, nodes):
        print(s)
        for i, d in enumerate(adj):
            for j, w in d.items():
                print(nodes[i]+'->'+nodes[j]+':'+str(w))

    def charIndConversion(self):
        char2ind = {'A':0, 'C':1, 'G':2, 'T':3}
        ind2char = {0:'A', 1:'C', 2:'G', 3:'T'}
        return char2ind, ind2char

    def singleSmallParsimony(self, n, adjC, adjP, adj, nodes, char2ind, ind2char, charInd):
        s = [[np.inf]*4 for _ in range(len(adjC))]
        backtrack = [[(-1, -1) for _ in range(4)] for __ in range(len(adjC))]
        processed = [0 for _ in range(len(adjC))]
        ripe = set()
        for i in range(n):
            s[i][char2ind[nodes[i][charInd]]] = 0
            processed[i] = 1
            if len(adjP[i]) > 0:
                ripe.add(adjP[i][0])

        while len(ripe) > 0:
            v = ripe.pop()
            for k in range(4):
                l = [s[adjC[v][0]][i] + (0 if k == i else 1) for i in range(4)]
                r = [s[adjC[v][1]][i] + (0 if k == i else 1) for i in range(4)]
                largmin = np.argmin(l)
                rargmin = np.argmin(r)
                backtrack[v][k] = (largmin, rargmin)
                s[v][k] = l[largmin] + r[rargmin]
            processed[v] = 1
            if len(adjP[v]) > 0 and all([processed[u] for u in adjC[adjP[v][0]]]):
                ripe.add(adjP[v][0])

        ind = np.argmin(s[v])
        nodes[v] += ind2char[ind]
        smin = s[v][ind]

        #dist = [np.inf] * len(adj)
        q = queue.Queue()
        #dist[v] = 0
        q.put((v, ind))
        while not q.empty():
            v, k = q.get()
            if len(adjC[v]) > 0:
                u, w = adjC[v]
                l, r = backtrack[v][k]

                if k != l:
                    adj[v][u] += 1
                    adj[u][v] += 1
                if k != r:
                    adj[v][w] += 1
                    adj[w][v] += 1
                if len(adjC[u]) > 0:
                    nodes[u] += ind2char[l]
                    nodes[w] += ind2char[r]
                    q.put((u, l))
                    q.put((w, r))
        return smin

    def runSmallParsimony(self, n ,adjC, adjP, adj, nodes):
        char2ind, ind2char = self.charIndConversion()
        s = 0
        for i in range(len(nodes[0])):
            s += self.singleSmallParsimony(n, adjC, adjP, adj, nodes, char2ind, ind2char, i)
        return s

if __name__ == "__main__":
    SmallParsimony()
