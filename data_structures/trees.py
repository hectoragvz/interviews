# Binary Search Tree

# Value, left child, right child - Node Class to build

# A sole node can be considered to be a tree already, that is the reason we´ll implement a BST and the Node class in one go.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Check for values recursively
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                # Recursion here
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                # Recursion here
                self.right.insert(value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True
        
    # Going left all the time if possible and only prints if cant go left any further (returns values in asc order)
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value, end="--")
        if self.right:
            self.right.inorder_traversal()

    # Prints every case
    def preorder_traversal(self):
        print(self.value, end="--")
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    # Go as deep as possible and only then print
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value, end="--")

        
tree = TreeNode(10)
tree.insert(5)
tree.insert(9)
tree.insert(22)
tree.insert(34)
tree.insert(2)
tree.insert(7)


print(tree.inorder_traversal())
print({tree.preorder_traversal()})
print(tree.postorder_traversal())
