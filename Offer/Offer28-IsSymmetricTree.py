# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return helper(p.left, q.right) and helper(p.right, q.left)
            return False

        if root:
            return helper(root.left, root.right)
        return True
