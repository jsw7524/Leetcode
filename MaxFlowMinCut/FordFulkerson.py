class Graph:
    def __init__(self, size):
        self.size = size
        self.capacity = [[0 for _ in range(size)] for _ in range(size)]
        self.flow = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self, u, v, w):
        self.capacity[u][v] = w

class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph
        self.size = graph.size
        self.parent = [-1] * self.size

    def bfs(self, s, t):
        visited = [False] * self.size
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for v in range(self.size):
                if visited[v] == False and self.graph.capacity[u][v] - self.graph.flow[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    self.parent[v] = u
                    if v == t:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        max_flow = 0

        while self.bfs(source, sink):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph.capacity[self.parent[s]][s] - self.graph.flow[self.parent[s]][s])
                s = self.parent[s]

            max_flow += path_flow

            v = sink
            while(v != source):
                u = self.parent[v]
                self.graph.flow[u][v] += path_flow
                self.graph.flow[v][u] -= path_flow
                v = self.parent[v]

        return max_flow

size = 6  # 節點數量
g1 = Graph(size)
g1.add_edge(0, 1, 16)
g1.add_edge(0, 2, 13)
g1.add_edge(1, 2, 10)
g1.add_edge(1, 3, 12)
g1.add_edge(2, 4, 14)
g1.add_edge(3, 2, 9)
g1.add_edge(3, 5, 20)
g1.add_edge(4, 3, 7)
g1.add_edge(4, 5, 4)

ff1 = FordFulkerson(g1)
source = 0  # 源點
sink = 5    # 匯點
assert 23==ff1.ford_fulkerson(source, sink)
#print("The maximum possible flow is %d " % ff1.ford_fulkerson(source, sink))
#####################################
size = 6  # 節點數量
g2 = Graph(size)
g2.add_edge(0, 1, 7)
g2.add_edge(0, 2, 7)
g2.add_edge(2, 1, 2)
g2.add_edge(1, 4, 7)
g2.add_edge(2, 4, 5)
g2.add_edge(1, 3, 2)
g2.add_edge(4, 3, 4)
g2.add_edge(3, 5, 10)
g2.add_edge(4, 5, 8)

ff2 = FordFulkerson(g2)
source = 0  # 源點
sink = 5    # 匯點
assert 14==ff2.ford_fulkerson(source, sink)
#print("The maximum possible flow is %d " % ff2.ford_fulkerson(source, sink))
##############
size = 4  # 節點數量
g3 = Graph(size)
g3.add_edge(0, 1, 100)
g3.add_edge(0, 2, 100)
g3.add_edge(1, 2, 100)
g3.add_edge(1, 3, 100)
g3.add_edge(2, 3, 100)

ff3 = FordFulkerson(g3)
source = 0  # 源點
sink = 3    # 匯點
assert 200==ff3.ford_fulkerson(source, sink)