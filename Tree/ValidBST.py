from Tree.PrintBST import PrintBST
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.last = None

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        result = self.isValidBST(root.left)
        if result is False:
            return False

        if self.last and self.last.val >= root.val:
            return False

        self.last = root
        return self.isValidBST(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(5)
    a = TreeNode(4)
    root.right = a
    a.left = TreeNode(3)
    a.right = TreeNode(6)

    PrintBST.printBST(root)
    solution = Solution()
    result = solution.isValidBST(root)
    print('Is valid BST:{}'.format(result))