from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findMin(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr


def search(root, val):
    if not root:
        return None
    if val < root.val:
        return search(root.left, val)
    elif val > root.val:
        return search(root.right, val)
    else:
        return root


def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root


def delete(root, val):
    if not root:
        return None
    if root.val < val:
        root.right = delete(root.right, val)
    if root.val > val:
        root.left = delete(root.left, val)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:
            node = min(root.right)
            root.val = node.val
            root.right = delete(root.right, node.val)
    return root


def dfs(root):
    # Traversing by depth
    if not root:
        return
    dfs(root.left)
    print(root.val)  # This line may vary if preorder, inorder, or postorder
    dfs(root.right)


def bfs(root):
    sol = deque()
    if root:
        sol.append(root)
    level = 0
    while len(sol) > 0:
        for i in range(len(sol)):
            curr = sol.popleft()
            if curr.left:
                sol.append(curr.left)
            if curr.right:
                sol.append(curr.right)
        level += 1
