from typing import List

from Tree.PrintBST import PrintBST


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://www.bilibili.com/video/BV12C4y1h7Ao?from=search&seid=17640066302150177237
    def generateTrees(self, n: int) -> List[TreeNode]:

        ans = []
        if n == 0:
            return ans

        def helper(start, end):
            ans = []
            if start > end:
                ans.append(None)
                return ans
            for i in range(start, end + 1):
                left = helper(start, i - 1)
                right = helper(i + 1, end)
                for node_l in left:
                    for node_r in right:
                        root = TreeNode(i)
                        root.left = node_l
                        root.right = node_r
                        ans.append(root)
            return ans

        return helper(1, n)


if __name__ == '__main__':
    solution = Solution()
    list_nodes = solution.generateTrees(3)
    for node in list_nodes:
        PrintBST.printBST(node)
