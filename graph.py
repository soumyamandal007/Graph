from LinkedList import LinkedList 

class Graph():
   def __init__(self,vertices):
      self.vertices = vertices
      self.array = []
      for i in range(vertices):
         self.array.append(LinkedList())
   
   def add_edge(self, source, destination):
      if (source < self.vertices and destination < self.vertices):
         self.array[source].insert_at_head(destination)
         
         
   def print_graph(self):
      print("--> Adjacency List is <--")
      for i in range(self.vertices):
         print(" | " , i , end=" | => ")
         curr = self.array[i].get_head()
         while curr:
            print("[" , curr.data , end = "] --> ")
            curr = curr.next
         print("None")
   
