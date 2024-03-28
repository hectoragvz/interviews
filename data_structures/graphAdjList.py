# Class implementation of graphs in an adjacency list approach


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = {}
        for node in self.nodes:
            self.adj_list[node] = []

    def get_list(self):
        for node in self.nodes:
            print(f"{node} -> {self.adj_list[node]}")

    def find_degree(self, node):
        degree = len(self.adj_list[node])
        print(degree)

    def add_edge(self, node1, node2):
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    def dfs(self, source):
      pass

    def bfs(self, source):
      pass


nodes1 = ["A", "B", "C", "D", "E"]
graph = Graph(nodes=nodes1)
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.get_list()
graph.bfs("A")
