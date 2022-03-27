
from collections import defaultdict,OrderedDict
from queue import PriorityQueue
"""
This code will help us to utilize a default dict to take input a graph's node and store.
Note that it will be only useful for an unweighted graph which means we assume each edge
has a weight 1.
"""
class Graph(object):
    def __init__(self):
        self.g = defaultdict(list)
        self.queue = []
        self.visited = []
        self.weight = defaultdict(list)
        self.cost = 0

    def printing(self):
        print(self.g)
        print(self.weight)


    def insert(self, node1, node2, weight):
        self.g[node1].append(node2)
        self.g[node2].append(node1)
        self.weight[(node1, node2)].append(weight)
        self.weight[(node2, node1)].append(weight)

    def prims(self, node):
        self.visited.append(node)
        tempNodes = [n for n in self.visited]
        tempDict = {}
        for n in tempNodes:
            for nn in self.g[n]:
                if n and nn not in self.visited:
                    tempDict[self.weight[(n,nn)][0]]=[n,nn]
        if tempDict:
            min_weight_edge = sorted(tempDict.items())[0][1]
            self.cost += sorted(tempDict.items())[0][0]
            self.prims(min_weight_edge[1])
        return self.visited, self.cost



gr = Graph()
gr.insert(1,2,7)
gr.insert(1,4,3)
gr.insert(1,5,12)
gr.insert(2,3,9)
gr.insert(4,3,7)
gr.insert(5,3,5)
# gr.printing()
print(gr.prims(1))
