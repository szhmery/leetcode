from Tree.PrintBST import PrintBST
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(5)
    a = TreeNode(4)
    root.right = a
    a.left = TreeNode(3)
    a.right = TreeNode(6)

    PrintBST.printBST(root)
    solution = Solution()
    result = solution.isValidBST(root)
    print('Is valid BST:{}'.format(result))

