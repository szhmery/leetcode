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
        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0
        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    root = solution.buildTree(preorder, inorder)
    print('method 1: buildTree:')
    PrintBST.printBST(root)
