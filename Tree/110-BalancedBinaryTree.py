from Tree.PrintBST import PrintBST


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://www.bilibili.com/video/BV1sV411b7hR
    # DFS
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if root is None:
                return True, 0
            bl, ll = dfs(root.left)
            if not bl:
                return False, 0
            br, lr = dfs(root.right)
            if not br:
                return False, 0
            return abs(ll - lr) <= 1, max(ll, lr) + 1

        return dfs(root)[0]


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    a = TreeNode(20)
    root.right = a
    a.left = TreeNode(15)
    a.right = TreeNode(7)

    PrintBST.printBST(root)
    solution = Solution()
    result = solution.isBalanced(root)
    print('is balanced:{}'.format(result))
