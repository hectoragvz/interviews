def invertTree(root):

    if not root:
        return None

    # Swap children
    tmp = root.left
    root.left = root.right
    root.right = tmp

    self.invertTree(root.left)
    self.invertTree(root.right)
    return root


print(invertTree(root=[4, 2, 7, 1, 3, 6, 9]))
