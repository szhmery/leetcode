from typing import List
from Tree.PrintBST import  PrintBST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        if root is None:
            return ans
        stack1 = []
        stack2 = []
        node = root
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node.val)
        # while stack2:
        #     ans.append(stack2.pop())
        return stack2[::-1]

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)
        ans = []
        postorder(root)
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(5)
    a = TreeNode(4)
    root.right = a
    a.left = TreeNode(3)
    a.right = TreeNode(6)
    PrintBST.printBST(root)
    solution = Solution()
    result = solution.postorderTraversal(root)
    print('post order BT:{}'.format(result))
    result = solution.postorderTraversal2(root)
    print('post order BT:{}'.format(result))
