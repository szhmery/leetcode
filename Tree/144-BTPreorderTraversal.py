from typing import List
from Tree.PrintBST import  PrintBST

# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # reiterate
    def preorderTraversal(self, root: 'Node') -> 'List[int]':
        stack = []
        ans = []
        if root is None:
            return ans

        node = root
        while node or stack:
            while node:
                ans.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return ans

    # recursion
    def preorderTraversal2(self, root: 'Node') -> 'List[int]':
        def preorder(root):
            if root is None:
                return
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)

        ans = []
        preorder(root)
        return ans


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(5)
    a = Node(4)
    root.right = a
    a.left = Node(3)
    a.right = Node(6)

    PrintBST.printBST(root)
    solution = Solution()
    result = solution.preorderTraversal(root)
    print('pre order BT:{}'.format(result))
    result = solution.preorderTraversal2(root)
    print('pre order BT:{}'.format(result))