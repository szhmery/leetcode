from queue import Queue

from Tree.PrintBST import PrintBST


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # BFS
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

    # recursion
    def levelOrder2(self, root: TreeNode) -> 'List[List[int]]':
        res = []
        self.preOrder(root, 0, res)
        return res

    def preOrder(self, node, level, res):
        if node:
            if len(res) < level + 1:
                res.append([])

            res[level].append(node.val)
            self.preOrder(node.left, level + 1, res)
            self.preOrder(node.right, level + 1, res)

    def printLevelOrder(self, root: TreeNode) -> 'List[int]':
        queue = Queue()
        queue.put(root)
        ans = []
        while queue.qsize() > 0: # must use qsize, if queue is emtpy, queue is not None
            tmp = queue.get()
            if tmp:
                ans.append(tmp.val)
                queue.put(tmp.left)
                queue.put(tmp.right)
        return ans


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
    print('method 1: Order traversal:')
    print(result)
    result = solution.levelOrder2(root)
    print('method 2: Order traversal:')
    print(result)

    print(solution.printLevelOrder(root))
