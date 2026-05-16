from collections import deque


def levelOrder(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """
    res = []
    if not root:
        return []
    q = deque()
    q.append(root)

    while q:
        level = []
        for i in range(len(q)):
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            level.append(curr.val)

        res.append(level)

    return res
