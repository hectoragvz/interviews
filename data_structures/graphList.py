# Graphs can be represented as an adjacency matrix or an adjacency list

# ADJACENCY LIST

def add_node(node):
  if node in graph.keys():
    print(f"{node} is in graph already")
  else:
    graph[node] = []

def add_edge(v1, v2, cost):
  if v1 not in graph:
    print("There is no node", v1)
  if v2 not in graph:
    print("There is no node", v2)
  else:
    # For adding costs
    list1 = [v2, cost]
    list2 = [v1, cost] # --delete if directed

    # If no cost just append v1 and v2
    graph[v2].append(list2) # --delete if directed
    graph[v1].append(list1)

    # If directed graph remove the list2 and graph[v2] lines since direction of graph is not bidirectional

graph = {} # or dict()

print(graph)
add_node("A")
add_node("B")
add_node("C")

add_edge("A", "C", 5)
print(graph)
