class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = Node(1)
    self.tail = self.head

  def is_empty(self):
    return self.head == None
  
  def size(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.next
    return count
  
  def append(self, val):
    new_node = Node(val)
    self.tail.next = new_node
    self.tail = self.tail.next

  def add(self, val):
    new_node = Node(val)
    new_node.next = self.head
    self.head = new_node

  def remove(self, index):
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
        curr = self.head.next
        while curr:
            print(curr.value, " -> ", end="")
            curr = curr.next
        print()