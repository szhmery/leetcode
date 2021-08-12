# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #recursion
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        root.left, root.right = root.right, root.left
        return root
    #iteration
    def mirrorTree2(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root
