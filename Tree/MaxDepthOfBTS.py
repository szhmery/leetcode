from Tree.PrintBST import PrintBST


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        leftmax = self.maxDepth(root.left)
        rightmax = self.maxDepth(root.right)
        return max(leftmax, rightmax) + 1


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    a = TreeNode(20)
    root.right = a
    a.left = TreeNode(15)
    a.right = TreeNode(7)

    PrintBST.printBST(root)
    solution = Solution()
    depth = solution.maxDepth(root)
    print('Depth:{}'.format(depth))
