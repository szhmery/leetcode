class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 树的遍历方式总体分为两类：深度优先搜索（DFS）、广度优先搜索（BFS）；
#
# 常见的 DFS ： 先序遍历、中序遍历、后序遍历；
# 常见的 BFS ： 层序遍历（即按层遍历）。


class Solution:
    # DFS
    #树的后序遍历，
    #时间复杂度 O(N) ： N 为树的节点数量，计算树的深度需要遍历所有节点。
    #空间复杂度 O(N) ： 最差情况下（当树退化为链表时），递归深度可达到 N 。
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # BFS
    #树的层次遍历。
    #时间复杂度O(N) ： NN 为树的节点数量，计算树的深度需要遍历所有节点。
    #空间复杂度O(N) ： 最差情况下（当树平衡时），队列 queue 同时存储 N/2 个节点。

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            res += 1
        return res
