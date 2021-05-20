from Tree.PrintBST import PrintBST
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://www.bilibili.com/video/BV1XZ4y1G7xM
    # BFS
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [(root, 1)]
        while q:
            cur, depth = q.pop(0)
            # left child and right child are both None, find the min depth
            if not cur.left and not cur.right:
                return depth
            if cur.left:
                q.append((cur.left, depth + 1))
            if cur.right:
                q.append((cur.right, depth + 1))




if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    a = TreeNode(20)
    root.right = a
    a.left = TreeNode(15)
    a.right = TreeNode(7)

    PrintBST.printBST(root)
    solution = Solution()
    result = solution.minDepth(root)
    print('is balanced:{}'.format(result))