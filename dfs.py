# Define a graph using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
visited = set()
stack = []
def dfs_traversal(graph, start):
   
   
   # visited.add(start)
   # stack.append(start)
   
   # while stack:
   #    node = stack.pop()
   #    if node not in visited:
   #       print(node , end='-->')
   #       visited.add(node)
   #    for neighbour in graph[node]:
   #       if neighbour not in visited:
   #          stack.append(neighbour)
   if start not in visited:
      visited.add(start)
      stack.append(start)
      while stack:
         node = stack.pop()
         print(node, end="-->")
         for neighbour in graph[node]:
            dfs_traversal(graph,neighbour)



print("Start traversing from 'A' DFS method ")
dfs_traversal(graph,'A')