class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def dfs(self):
        if not self:
            return []
        stack = [self]
        result = []
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result

    def rec_dfs(self, res=[]):
        if not self:
            return []
        res.append(self.val)
        if self.left:
            self.left.rec_dfs()
        if self.right:
            self.right.rec_dfs()
        return res

    def bfs(self):
        if not self:
            return []
        stack = [self]
        result = []
        while stack:
            curr = stack.pop(0)
            result.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return result


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


# print("Recursive DFS traversal:", a.rec_dfs())
# print("DFS Traversal:", a.dfs())
# print("BFS Traversal:", a.bfs())
