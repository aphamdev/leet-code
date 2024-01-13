class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_values(head):
  values = []
  #set current to point at the head
  current = head
  #while the current is not None
  # add the value of current to the values list
  while current is not None:
    values.append(current.val) 
    #move out current to the next node
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