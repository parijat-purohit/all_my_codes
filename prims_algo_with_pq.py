"""
Using priorityqueue for better time complexity
"""
from collections import defaultdict
from queue import PriorityQueue

class Graph(object):
    def __init__(self):
        self.g = defaultdict(list)
        self.visited = []
        self.nodes = []
        self.weight = PriorityQueue()
        self.cost = 0

    def printing(self):
        print(self.g)

    def insert(self, node1, node2, weight):
        self.g[node1].append(node2)
        self.g[node2].append(node1)
        if node1 not in self.nodes:
            self.nodes.append(node1)
        if node2 not in self.nodes:
            self.nodes.append(node2)
        self.weight.put([weight, node1, node2])
        self.weight.put([weight, node2, node1])

    def prims(self):
        if not self.visited:
            self.visited.append(self.nodes[0])
        unvisited = list(set(self.nodes)-set(self.visited))
        tempq = []
        while(self.weight):
            mwedge = self.weight.get()
            if(mwedge[1] in self.visited and mwedge[2] in unvisited):
                self.cost += mwedge[0]
                self.visited.append(mwedge[2])
                print(f'path {mwedge[1]}-{mwedge[2]}')
                break
            else:
                tempq.append(mwedge)
                # print(tempq)
        if tempq:
            for temp in tempq:
                self.weight.put(temp)
        if len(self.nodes)!=len(self.visited):
            self.prims()
        return self.cost


gr = Graph()
gr.insert(1,2,7)
gr.insert(1,4,3)
gr.insert(1,5,12)
gr.insert(2,3,9)
gr.insert(4,3,7)
gr.insert(5,3,5)
gr.printing()
print(gr.prims())
