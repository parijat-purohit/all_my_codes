from collections import defaultdict
"""
This code will help us to utilize a default dict to take input a graph's node and store.
Note that it will be only useful for an unweighted graph which means we assume each edge
has a weight 1.
"""
class Graph(object):
    def __init__(self):
        self.g = defaultdict(list)

    def insert(self, node1, node2):
        self.g[node1].append(node2)

    def full_graph(self):
        print(dict(self.g))

    def edges_of_a_node(self, node):
        if self.g[node]:
            for n in self.g[node]:
                print(node, n)
  


gr = Graph()
gr.insert(1,2)
gr.insert(1,3)
gr.insert(2,3)
gr.insert(2,5)
gr.insert(2,7)
gr.insert(5,8)
gr.full_graph()
gr.edges_of_a_node(1)
