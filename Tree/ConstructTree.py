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
        preorder_index = 0
        inorder_index_dict = {}
        for index, value in enumerate(inorder):
            inorder_index_dict[value] = index

        def ArrayToTree(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            node_value = preorder[preorder_index]
            root = TreeNode(node_value)
            preorder_index += 1
            root.left = ArrayToTree(left, inorder_index_dict[node_value] - 1)
            root.right = ArrayToTree(inorder_index_dict[node_value] + 1, right)
            return root

        return ArrayToTree(0, len(preorder) - 1)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    root = solution.buildTree(preorder, inorder)
    print('method 1: buildTree:')
    PrintBST.printBST(root)
