# Define a graph using an adjacency list
from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs_traversal(graph, start):
   visited = set()
   queue = deque()
   
   visited.add(start)
   queue.append(start)
   print(start,end='-->')
   while queue:
      node = queue.popleft()
      if node not in visited:
         print(node , end = '-->')
         visited.add(node)
      for neighbour in graph[node]:
         if neighbour not in visited:
            queue.append(neighbour)


print("Start traversing from 'A' BFS method ")
bfs_traversal(graph,'A')