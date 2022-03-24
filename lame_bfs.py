from collections import defaultdict
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

    def insert(self, node1, node2):
        self.g[node1].append(node2)

    def bfs(self, node):
        self.visited.append(node)
        self.queue.extend(self.g[node])
        while(self.queue):
            n = self.queue[0]
            self.queue = self.queue[1:]
            if n not in self.visited:
                self.visited.append(n)
                self.queue.extend(self.g[n])
        return self.visited

gr = Graph()
gr.insert(1,2)
gr.insert(2,3)
gr.insert(1,3)
gr.insert(2,5)
gr.insert(2,7)
gr.insert(5,8)
print(gr.bfs(1))
