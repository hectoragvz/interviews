# Graphs can be represented as an adjacency matrix or an adjacency list

# ADJACENCY MATRIX representation (nested list)
nodes = []
graph = [] # will be later the nested list
node_count = 0

def add_node(node):
  global node_count
  if node in nodes:
    print("Node already in graph")
  else:
    nodes.append(node)
    node_count += 1

    # Adding column and row to the graph representing the added node
    for n in graph:
      n.append(0)
    # Adding a value(row) for each column
    temp = []
    for i in range(node_count):
      temp.append(0)
    graph.append(temp)

def print_graph():
  for i in range(node_count):
    for j in range(node_count):
      print(format(graph[i][j], "<3"), end=" ")
    print()


def add_edge(node1, node2, cost):
  if node1 not in nodes:
    print(f"{node1} not in graph")
  elif node2 not in nodes:
    print(f"{node2} not in graph")
  else:
    index1 = nodes.index(node1)
    index2 = nodes.index(node2)
    graph[index1][index2] = cost
    graph[index2][index1] = cost # this line disappears for directed graphs


print("Before addtion")
print(nodes)
print(graph)

add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 2)

print("After addtion")
print(nodes)
print(graph)
print_graph()