from Tree.PrintBST import PrintBST
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # https://www.bilibili.com/video/BV1r7411Z7fF?from=search&seid=16570887184197918265
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        cur = []
        def DFS(root, cur, ans):
            if not root:
                return
            if not root.left and not root.right:
                cur.append(str(root.val))
                ans.append('->'.join(cur))
                cur.pop()
                return
            cur.append(str(root.val))
            DFS(root.left, cur, ans)
            DFS(root.right, cur, ans)
            cur.pop()
        DFS(root, cur, ans)
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    a = TreeNode(2)
    root.left = a
    a.left = TreeNode(4)
    a.right = TreeNode(5)

    PrintBST.printBST(root)
    solution = Solution()
    result = solution.binaryTreePaths(root)
    print('BST path:{}'.format(result))

