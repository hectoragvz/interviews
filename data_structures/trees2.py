# Implementing BST again to practice
# Since a node is considered a BST

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def find(self, value):
    if self.value == value:
      return True
    elif value < self.value:
      if self.left is None:
        return False
      else:
        return self.left.find(value)
    else:
      if self.right is None:
        return False
      return self.right.find(value)

  def insert(self, value):
    # Empty?
    if self.value is None:
      self.value = value
      return
    if value < self.value:
      if self.left is None:
        self.left = TreeNode(value)
      else:
        self.left.insert(value)
    else:  
      if self.right is None:
        self.right = TreeNode(value)
      else:
        self.right.insert(value)

  def preorder_traversal(self):
    print(self.value, end="-")
    if self.left is not None:
      self.left.preorder_traversal()
    if self.right is not None:
      self.right.preorder_traversal()

  def inorder_traversal(self):
    if self.left is not None:
      self.left.inorder_traversal()
    print(self.value, end="-")
    if self.right is not None:
      self.right.inorder_traversal()

  def postorder_traversal(self):
    if self.left is not None:
      self.left.postorder_traversal()
    if self.right is not None:
      self.right.postorder_traversal()
    print(self.value, end="-")

  def deleteNode(self, value):
    # Is the tree empty?
    if self.value is None:
      print("Empty tree")
      return
    if value < self.value:
      if self.left:
        self.left = self.left.deleteNode(value)
      else:
        print("Given node not present tree")
    elif value > self.value:
      if self.right:
        self.right = self.right.deleteNode(value)
      else:
        print("Given node not present tree")
    else:
      # We´ve arrived at the node we want to delete (it may have 0, 1, or 2 children)
      # 0 OR 1 CHILDREN
      # If we can´t find a left or right child, return whatever (head of other part more concisely) is in the other half of the node basically
      if self.left is None:
        temp = self.right
        self = None
        return temp
      if self.right is None:
        temp = self.left
        self = None
        return temp
      # 2 CHILDREN
      # You can either replace the node with the greatest value in the left subtree or the smallest value in the right subtree (to keep BST properties)
      # I´ll take the smallest value in the right subtree here 
      node = self.right
      # While there is a smallest value present ...
      while node.left:
        # Keep assigning the value to the node we want
        node = node.left
      # We´ve now find the smallest node value in the right subtree
      self.value = node.value
      self.right = self.rigth.deleteNode(node.value)
    return self

root = TreeNode(10)
numbers = [1,2,3,4,5,9,12,76]
for i in numbers:
  root.insert(i)


""" print(root.preorder_traversal())
print(root.inorder_traversal())
print(root.postorder_traversal()) """

print(root.preorder_traversal())
root.deleteNode(12)
print(root.preorder_traversal())