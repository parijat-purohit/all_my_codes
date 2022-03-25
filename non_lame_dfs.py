from collections import defaultdict
"""
This code will help us to utilize a default dict to take input a graph's node and store.
Note that it will be only useful for an unweighted graph which means we assume each edge
has a weight 1.
"""
class Graph(object):
    def __init__(self):
        self.g = defaultdict(list)
        self.stack = []
        self.visited = []

    def insert(self, node1, node2):
        self.g[node1].append(node2)

    def dfs(self, node):
        self.visited.append(node)
        self.stack.extend(self.g[node][::-1])
        if self.stack:
            n = self.stack.pop()
            return self.dfs(n)
        return self.visited

gr = Graph()
gr.insert(1,2)
gr.insert(1,4)
gr.insert(1,5)
gr.insert(2,6)
gr.insert(2,7)
gr.insert(2,3)
print(gr.dfs(1))
