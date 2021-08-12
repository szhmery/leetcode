# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, a: TreeNode, b: TreeNode) -> bool:
        if not a and not b:
            return True
        if a and b and a.val == b.val:
            return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
        else:
            return False

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        return p.val == q.val and self.isSameTree2(p.left, q.left) and self.isSameTree2(p.right, q.right)
