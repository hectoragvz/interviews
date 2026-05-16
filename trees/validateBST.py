def isValidBST(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """

    def valid(node, leftValue, rightValue):
        if not node:
            return True
        if not (node.val < rightValue and node.val > leftValue):
            return False

        return valid(node.left, leftValue, node.val) and valid(
            node.right, node.val, rightValue
        )

    return valid(root, float("-inf"), float("inf"))
