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



root = TreeNode(10)
numbers = [1,2,3,4,5,9,12,76]
for i in numbers:
  root.insert(i)

print(root.find(76))

""" print(root.preorder_traversal())
print(root.inorder_traversal())
print(root.postorder_traversal()) """
