"""
Without ranking, random assignment of parents would actually result a graph actually with cycle there. I just implemented it for focusing on the fault.
I used here disjoint set and path compression. But still it doesn't produce minimum spanning tree. Hopefully, my next version would solve the problem.
"""
from queue import PriorityQueue

class Graph(object):
    def __init__(self):
        self.weight = PriorityQueue()
        self.cost = 0
        self.parent = {}
        self.no_edge = 0

    def insert(self, node1, node2, weight):
        self.weight.put([weight, node1, node2])
        self.weight.put([weight, node2, node1])
        self.parent[node1] = node1
        self.parent[node2] = node2

    def findparent(self, node):
        if self.parent[node] == node:
            return node
        else:
            self.parent[node] = self.findparent(self.parent[node])
            return self.parent[node]

    def kruskal(self):
        while(not self.weight.empty()):
            min_edge = self.weight.get()
            u = self.findparent(min_edge[1])
            v = self.findparent(min_edge[2])
            if(u!=v):
                self.parent[min_edge[2]] = min_edge[1]
                print(f'path printing {min_edge[1]} - {min_edge[2]}')
                self.cost+=min_edge[0]
        return self.cost


gr = Graph()
gr.insert(0, 1, 4)
gr.insert(0, 7, 8)
gr.insert(1, 2, 8)
gr.insert(1, 7, 11)
gr.insert(6, 7, 1)
gr.insert(7, 8, 7)
gr.insert(2, 3, 7)
gr.insert(2, 5, 4)
gr.insert(2, 8, 2)
gr.insert(6, 8, 6)
gr.insert(6, 5, 2)
gr.insert(3, 5, 14)
gr.insert(3, 4, 9)
gr.insert(5, 4, 10)
print(gr.kruskal())
