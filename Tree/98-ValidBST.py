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

    # https://www.bilibili.com/video/BV1Vb411V74h?from=search&seid=10476592804165224680
    def isValidBST2(self, root: TreeNode) -> bool:
        def helper(root, minval=-float('inf'), maxval=float('inf')):
            if root is None:
                return True
            if not minval < root.val < maxval:
                return False
            return helper(root.left, minval, root.val) and helper(root.right, root.val, maxval)

        return helper(root)

    #https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)
    def isValidBST3(self, root: TreeNode) -> bool:
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(5)
    a = TreeNode(4)
    root.right = a
    a.left = TreeNode(3)
    a.right = TreeNode(6)

    PrintBST.printBST(root)
    solution = Solution()
    result = solution.isValidBST3(root)
    print('Is valid BST:{}'.format(result))

    result = solution.isValidBST3(root)
    print('Is valid BST:{}'.format(result))