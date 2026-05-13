class Solution:
    def inorderTraversal_recursive(self, root):
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        return res

    def inorderTraversal_iterative(self, root):
        res, stack = [], []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

    def inorderTraversal(self, root):
        return self.inorderTraversal_iterative(root)