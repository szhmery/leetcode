from typing import List
from Tree.PrintBST import PrintBST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, postorder, inorder, len(postorder), 0, len(inorder))

    def buildTreeRecu(self, lookup, postorder, inorder, post_end, in_start, in_end):
        if in_start == in_end:
            return None
        node = TreeNode(postorder[post_end - 1])
        i = lookup[postorder[post_end - 1]]
        node.left = self.buildTreeRecu(lookup, postorder, inorder, post_end - 1 - (in_end - i - 1), in_start, i)
        node.right = self.buildTreeRecu(lookup, postorder, inorder, post_end - 1, i + 1, in_end)
        return node

    # https://www.bilibili.com/video/BV1jh411Z7y8?from=search&seid=11401641767475906326
    def buildTree2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(ini, inj, posti, postj):
            if ini == inj:
                return TreeNode(inorder[ini])
            rootval = postorder[postj]
            ind = dic[rootval]
            res = TreeNode(rootval)

            leftin1 = ini
            rightin1 = ind - 1
            leftpost1 = posti
            rightpost1 = posti + rightin1 - leftin1

            leftin2 = ind + 1
            rightin2 = inj
            leftpost2 = rightpost1 + 1
            rightpost2 = postj - 1

            if rightin1 >= leftin1:
                res.left = build(leftin1, rightin1, leftpost1, rightpost1)
            if rightin2 >= leftin2:
                res.right = build(leftin2, rightin2, leftpost2, rightpost2)
            return res



        if not inorder:
            return None
        dic = {n: i for i, n in enumerate(inorder)}
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)


if __name__ == '__main__':
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    solution = Solution()
    root = solution.buildTree(inorder, postorder)
    print('method 1: buildTree:')
    PrintBST.printBST(root)
    root = solution.buildTree2(inorder, postorder)
    print('method 2: buildTree:')
    PrintBST.printBST(root)