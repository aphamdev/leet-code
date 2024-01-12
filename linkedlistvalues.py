class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_values(head):
  values = []
  current = head
  while current is not None:
    values.append(current.val) 
    current = current.next
  return values
    
    
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_values(a)) # -> [ 'a', 'b', 'c', 'd' ]