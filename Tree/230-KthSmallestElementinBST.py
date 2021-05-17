# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://www.bilibili.com/video/BV1ha4y1i7dZ?from=search&seid=12006647812838421020
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inOrder_recursion(root):
            if not root:
                return None
            res = inOrder_recursion(root.left)
            if res is not None:
                return res
            self.k -= 1
            if self.k == 0:
                return root.val
            else:
                return inOrder_recursion(root.right)

        self.k = k
        # return inOrder_recursion(root)

        return inOrder_recursion(root)
    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        stack = []
        if root is None:
            return

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right




