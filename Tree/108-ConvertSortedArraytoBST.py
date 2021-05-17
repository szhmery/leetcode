from typing import List
from Tree.PrintBST import PrintBST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        return TreeNode(val=nums[mid],
                        left=self.sortedArrayToBST(nums[:mid]),
                        right=self.sortedArrayToBST(nums[mid + 1:]))


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    solution = Solution()
    bst = solution.sortedArrayToBST(nums)

    PrintBST.printBST(bst)
