from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    #BFS
    # https://www.bilibili.com/video/BV1yK411n76R
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans, q = [], [root]
        if root is None:
            return ans
        while q:
            val, tmp = [], []
            for node in q:
                val.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp
            ans.append(val)
        return ans[::-1]