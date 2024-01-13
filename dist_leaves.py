from queue import Queue
#define bfs
def bfs(tree, root) :
    queue = Queue()
    dist_list, dist_list[root], current_node = [-99] * len(tree), 0, root

    #for each leaf, find the dist btwn all other nodes
    for [neighbour, weight] in tree[current_node] :
        dist_list[neighbour] = dist_list[current_node] + weight
        queue.put(neighbour)

    while not queue.empty() :
        current_node = queue.get()
        for [neighbour, weight] in tree[current_node] :
            if dist_list[neighbour] == -99 :
                dist_list[neighbour] = dist_list[current_node] + weight
                #print(queue)
                queue.put(neighbour)
                #print(queue)
            else :
                continue

    return dist_list
##################################################
#defaultdict prevents keyerror :0 since each ke has defalut value if not yet assigned
from collections import defaultdict
tree = defaultdict(list)

with open("rosalind_ba7a.txt") as file :
    num_leaves = int(file.readline())
    #print(num_leaves)
    for line in file.readlines() :
        source, destination, weight = list(map(int, line.replace("->", " ").replace(":", " ").split()))
        tree[source].append([destination, weight])
        #print(tree)
[print(" ".join(list(map(str, bfs(tree, i)[:num_leaves])))) for i in range(num_leaves)]
