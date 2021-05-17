from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if root is None:
            return ans

        # 0 represents from left to right, otherwise 1 means from right to left
        zigzag = 0
        q = [root]
        while len(q) != 0:
            values = [node.val for node in q]
            if zigzag:
                values.reverse()
            ans.append(values)
            zigzag = ~zigzag
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
                q = new_q

        return ans

    def zigzagLevelOrder2(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.preOrder(root, 0, res)
        return res

    def preOrder(self, node, level, res):
        if node:
            if len(res) < level + 1:
                res.append([])
            if level % 2 != 0:
                res[level].insert(0, node.val)
            else:
                res[level].append(node.val)
            self.preOrder(node.left, level + 1, res)
            self.preOrder(node.right, level + 1, res)


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

    solution = Solution()
    result = solution.zigzagLevelOrder(root)
    print('method 1: ZigZag traversal:')
    print(result)
    result = solution.zigzagLevelOrder2(root)
    print('method 2: ZigZag traversal:')
    print(result)

    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    root.left = a
    root.right = b
    a.left = TreeNode(4)
    a.right = TreeNode(5)

    solution = Solution()
    result = solution.zigzagLevelOrder(root)
    print('method 1: ZigZag traversal:')
    print(result)
    result = solution.zigzagLevelOrder2(root)
    print('method 2: ZigZag traversal:')
    print(result)