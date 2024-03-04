# Reimplementing linked lists

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Linked_List:
  def __init__(self):
    self.head = Node(1)
    self.tail = self.head

  def add(self, data):
    node = Node(data)
    node.next = self.head
    self.head = node

  def is_empy(self):
    return self.head == None
  
  def size(self):
    count = 0
    current = self.head
    while current:
      count += 1
      current = current.next
    return count
  
  def append(self, data):
    node = Node(data)
    self.tail.next = node
    self.tail = self.tail.next
  
  def delete(self, index):
    i = 0
    current = self.head
    while i < index and current:
      i += 1
      current = current.next
    
    if current and current.next:
      if current.next == self.tail:
        self.tail = current
      current.next = current.next.next

  def print(self):
        """
        Returns a string representation of the list on O(n)
        e.g. [Head: 3]->[2]->[Tail: 1]
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"Head: {current.data}")
            elif current.next is None:
                nodes.append(f"Tail: {current.data}")
            else:
                nodes.append(f"{current.data}")

            current = current.next
        return "->".join(nodes)



li = Linked_List()

node1 = Node(1)
node2 = Node(2)

li.add(Node(5))
li.add(node1)
li.append(node2) 

print(li.size())

print(li.print())

