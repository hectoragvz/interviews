graph = {
  "A" : ["B", "D"],
  "B" : [],
  "C" : [],
  "D" : ["E", "G"],
  "E" : ["C"],
  "F" : [],
  "G" : ["F"]
}


# DFS Traversal - Stack Data Structure

def dfs(graph, source):
  stack = []
  stack.append(source)

  while stack:
    node = stack.pop(-1)
    print(node)
    for neighbor in graph[node]:
      stack.append(neighbor)


# BFS Traversal - Stack Data Structure

def bfs(graph, source):
  queue = []
  queue.append(source)

  while queue:
    node = queue.pop(0)
    print(node)
    for neighbor in graph[node]:
      queue.append(neighbor)


print("DFS")
dfs(graph, "A")
print("BFS")
bfs(graph, "A")
