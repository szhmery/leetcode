from Tree.PrintBST import PrintBST


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> 'List[List[int]]':
        res = []
        if root is None:
            return res

        q = [root]
        while len(q) != 0:
            res.append([node.val for node in q])
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q

        return res


if __name__ == '__main__':
    root = TreeNode(3)
    a = TreeNode(9)
    b = TreeNode(20)
    root.left = a
    root.right = b
    # a.left = TreeNode()
    # a.right = TreeNode()
    b.left = TreeNode(15)
    b.right = TreeNode(7)

    PrintBST.printBST(root)
    solution = Solution()
    result = solution.levelOrder(root)
    print('Order traversal:')
    print(result)
