# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # DFS
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return
        if not left:
            return right
        if not right:
            return left
        return root

    # save parent nodes
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def saveParent(node):
            if node.left:
                parent[node.left.val] = node
                saveParent(node.left)

            if node.right:
                parent[node.right.val] = node
                saveParent(node.right)

        parent = {}
        parent[root.val] = None
        visited = {}
        saveParent(root)
        while p:
            visited[p.val] = True
            p = parent[p.val]
        while q:
            if visited[q.val]:
                ans = parent[q.val]
                break
            else:
                q = parent[q.val]
        return ans
