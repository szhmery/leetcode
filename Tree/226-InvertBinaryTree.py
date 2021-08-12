# Definition for a binary tree node.
from Tree.PrintBST import PrintBST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # https://leetcode.com/problems/invert-binary-tree/solution/
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

    def invertTree2(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        stack = []

        stack.append(root)
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root



if __name__ == '__main__':
    root = TreeNode(1)

    b = TreeNode(2)
    b.left = TreeNode(1)
    b.right = TreeNode(3)
    root.left = b
    a = TreeNode(7)
    root.right = a
    a.left = TreeNode(6)
    a.right = TreeNode(9)
    PrintBST.printBST(root)
    solution = Solution()
    node = solution.invertTree(root)
    PrintBST.printBST(node)
    node = solution.invertTree2(root)
    PrintBST.printBST(node)




