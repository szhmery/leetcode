from typing import List
import collections

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #时间复杂度 O(N) ： N 为二叉树的节点数量，即 BFS 需循环 N 次。
    #空间复杂度 O(N) ： 最差情况下，即当树为平衡二叉树时，最多有 N/2 个树节点同时在 queue 中，使用 O(N) 大小的额外空间。
    # BFS
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        #Python 中使用 collections 中的双端队列 deque() ，其 popleft() 方法可达到 O(1) 时间复杂度；
        # 列表 list 的 pop(0) 方法时间复杂度为 O(N) 。
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

