from Tree.PrintBST import PrintBST


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS
    # https://www.bilibili.com/video/BV1WV411a7VR
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.res += node.val
                if node.val > low:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        self.res = 0
        dfs(root)
        return self.res


if __name__ == '__main__':
    root = TreeNode(10)
    l = TreeNode(5)
    l.left = TreeNode(3)
    l.right = TreeNode(7)
    root.left = l
    r = TreeNode(15)
    root.right = r
    r.right = TreeNode(18)

    PrintBST.printBST(root)
    solution = Solution()

    result = solution.rangeSumBST(root, 7, 15)
    print(result)
