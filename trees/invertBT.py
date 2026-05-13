def invertTree(root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """
    if not root:
        return None

    temp = root.left
    root.left = root.right
    root.right = temp

    invertTree(root.left)
    invertTree(root.right)

    return root
