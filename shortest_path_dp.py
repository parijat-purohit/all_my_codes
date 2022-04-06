"""
This DP is very interesting in nature. This code actually calculates in a DAG from a shortest path from a route node to
the destination node. here if you have 5 nodes in graph ranging from 0,1,2,3,4 then we can calculate anything 0-2, 1-4
etc. res[0], res[1], res[2] etc are giving us the cost of the shortest path for 0-4, 1-4, 2-4 respectively.

"""
inf = 99999
class Graph(object):
    def __init__(self):
        self.nodes = []
        self.weight = {}
        self.res = [-1]*1000

    def insert(self, node1, node2, weight):
        if node1 not in self.nodes:
            self.nodes.append(node1)
        if node2 not in self.nodes:
            self.nodes.append(node2)
        self.weight[node1, node2] = weight

    def printing(self):
        print(self.weight)
        # print(self.nodes)

    def shortest_path(self, u, n):
        if u==n:
            return 0
        if self.res[u]!=-1:
            return self.res[u]

        ans = inf
        for v in self.nodes:
            if (u,v) in self.weight.keys():
                ans = min(ans, self.shortest_path(v,n) + self.weight[u,v])
        self.res[u] = ans
        return self.res[u]

gr = Graph()
gr.insert(0, 1, 4)
gr.insert(1, 2, 8)
gr.insert(1, 4, 4)
gr.insert(4, 5, 10)
gr.insert(2, 5, 1)
gr.printing()
print(gr.shortest_path(1,5))
# res[2] is storing the shortest path cost from 2 to 5.
print(gr.res[2])
