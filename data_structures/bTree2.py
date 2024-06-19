class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def dfs(self):
        if not self:
            return None
        stack = [self]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res

    def bfs(self):
        if not self:
            return []
        queue = [self]
        res = []

        while queue:
            curr = queue.pop(0)
            res.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return res


a = TreeNode("a")
b = TreeNode("b")
c = TreeNode("c")
d = TreeNode("d")
e = TreeNode("e")
f = TreeNode("f")
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print("DFS Traversal:", a.dfs())
print("BFS Traversal:", a.bfs())
