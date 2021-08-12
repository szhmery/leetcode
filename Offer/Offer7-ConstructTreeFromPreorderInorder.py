from typing import List
from Tree.PrintBST import PrintBST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not (preorder and inorder):
            return
        root = TreeNode(preorder[0])
        mid_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid_index + 1], inorder[:mid_index])
        root.right = self.buildTree(preorder[mid_index + 1:], inorder[mid_index + 1:])
        return root

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(left, right):
            nonlocal pre_index
            if left > right:
                return
            root_value = preorder[pre_index]
            root = TreeNode(preorder[pre_index])

            pre_index += 1

            root.left = build(left, inorder_index_map[root_value] - 1)
            root.right = build(inorder_index_map[root_value] + 1, right)
            return root

        pre_index = 0
        inorder_index_map = {value: index for index, value in enumerate(inorder)}
        return build(0, len(preorder) - 1)

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    root = solution.buildTree(preorder, inorder)
    print('method 1: buildTree:')
    PrintBST.printBST(root)
    preorder = [1, 2, 3, 4, 5, 6, 7]
    inorder = [3, 2, 4, 1, 6, 5, 7]
    root = solution.buildTree2(preorder, inorder)
    print('method 2: buildTree:')
    PrintBST.printBST(root)