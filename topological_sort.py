from collections import defaultdict
from queue import PriorityQueue

class Graph(object):
    def __init__(self):
        self.g = defaultdict(list)
        self.rank = defaultdict(int)
        self.nodes = set()
        self.visited = []


    def insert(self, node1, node2):
        self.g[node1].append(node2)
        self.nodes.add(node1)
        self.nodes.add(node2)
        if node2 not in self.rank:
            self.rank[node2] = 1
        else:
            self.rank[node2] += 1

    def toposort(self):
        for n in self.nodes:
            if n not in self.visited and self.rank[n]==0:
                current_node = n
                break
        self.visited.append(current_node)

        for x in self.g[current_node]:
            self.rank[x] -= 1

        del self.g[current_node]
        del self.rank[current_node]

        while(len(self.visited)!=len(self.nodes)):
            self.toposort()

        return self.visited

gr = Graph()
gr.insert(1,2)
gr.insert(1,3)
gr.insert(2,5)
gr.insert(2,4)
gr.insert(3,4)
gr.insert(4,5)
print(gr.toposort())
