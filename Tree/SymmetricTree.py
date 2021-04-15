from Tree.PrintBST import PrintBST


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    def help(self, p, q):
        if p is None and q is None: return True
        if p and q and p.val == q.val:
            return self.help(p.right, q.left) and self.help(p.left, q.right)
        return False

    def isSymmetric(self, root):
        if root:
            return self.help(root.left, root.right)
        return True


if __name__ == '__main__':
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(2)
    root.left = a
    root.right = b
    a.left = TreeNode(4)
    a.right = TreeNode(3)
    b.left = TreeNode(3)
    b.right = TreeNode(4)

    PrintBST.printBST(root)
    solution = Solution()
    result = solution.isSymmetric(root)
    print('Is symmetric tree:{}'.format(result))
