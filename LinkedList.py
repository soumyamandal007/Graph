from Node import Node

class LinkedList():
   def __init__(self):
      self.head_node = None
      
   def get_head(self):
      return self.head_node
      
   def length(self):
      curr = self.get_head()
      length = 0
      while curr is not None:
         length += 1
         curr = curr.next
      pass
   
   def is_Empty(self):
      if self.head_node is None:
         return True
      else:
         return False
      
   def insert_at_head(self,dt):
      new_head_node = Node(dt)
      if (self.is_Empty()):
         self.head_node = new_head_node
         return self.head_node
      new_head_node.next = self.head_node
      self.head_node = new_head_node
      return self.head_node
   
   def insert_at_tail(self,dt):
      new_node = Node(dt)
      if self.get_head() is None:
         self.head_node = new_node
         return
      curr = self.get_head()
      while curr is not None:
         curr = curr.next
      curr.next = new_node
      return

   def print_list(self):
      if self.is_Empty():
         print("List is Empty")
         return False
      curr = self.get_head()
      while curr is not None:
         print(curr.data, end = "----> ")
         curr = curr.next
      print(curr.data,"--->None")
      return True
   
   
   def delete_at_head(self):
      first_element = self.get_head()
      if first_element is not None:
         self.head_node = first_element.next
         first_element.next = None
      return 
   
   def delete(self,dt):
      if self.is_Empty():
         print("List is Empty")
         return False
      curr = self.get_head()
      prev_node = None
      if curr.data == dt:
         self.delete_at_head()
         return True
      while curr is not None:
         if curr.data == dt:
            prev_node.next = curr.next
            curr.next = None
            break
         prev_node = curr
         curr = curr.next
      return True
   
   def search(self,dt):
      pass
   
   