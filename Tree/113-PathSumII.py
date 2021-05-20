from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # https://www.bilibili.com/video/BV1U7411o7i2?from=search&seid=8533814937093427041
    # DFS
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []
        self.DFS(root, targetSum, [], ans)
        return ans

    def DFS(self, node, num, res, ans):
        if node is None:
            return

        if not node.left and not node.right:
            if node.val == num:
                res.append(node.val)
                ans.append(res[:])
                res.pop()
                return
        res.append(node.val)
        self.DFS(node.left, num - node.val, res, ans)
        self.DFS(node.right, num - node.val, res, ans)
        res.pop()
        return
