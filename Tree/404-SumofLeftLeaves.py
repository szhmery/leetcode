from Tree.PrintBST import PrintBST


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
                if node and not node.left and not node.right:
                    ans += node.val
            node = stack.pop()
            node = node.right
        return ans

    # https://www.bilibili.com/video/BV15a4y1779U
    def sumOfLeftLeaves2(self, root: TreeNode) -> int:
        def dfs(root, flag):
            if not root:
                return 0
            if flag and not root.left and not root.right:
                return root.val
            return dfs(root.left, True) + dfs(root.right, False)

        return dfs(root, False)


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    a = TreeNode(2)
    root.left = a
    a.left = TreeNode(4)
    a.right = TreeNode(5)

    PrintBST.printBST(root)
    solution = Solution()
    result = solution.sumOfLeftLeaves(root)
    print('sum of left leaves:{}'.format(result))
    result = solution.sumOfLeftLeaves2(root)
    print('sum of left leaves:{}'.format(result))

    root = TreeNode(3)
    b = TreeNode(20)
    root.right = b
    a = TreeNode(9)
    root.left = a
    b.left = TreeNode(15)
    b.right = TreeNode(7)

    PrintBST.printBST(root)
    result = solution.sumOfLeftLeaves(root)
    print('sum of left leaves:{}'.format(result))

    result = solution.sumOfLeftLeaves2(root)
    print('sum of left leaves:{}'.format(result))
