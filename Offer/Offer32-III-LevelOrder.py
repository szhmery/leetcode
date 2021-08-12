from typing import List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # BFS
    #时间复杂度 O(N) ： N 为二叉树的节点数量，即 BFS 需循环 N 次，占用 O(N) ；
    # 双端队列的队首和队尾的添加和删除操作的时间复杂度均为 O(1) 。
    # 空间复杂度 O(N) ： 最差情况下，即当树为满二叉树时，最多有 N/2 个树节点 同时 在 deque 中，
    # 使用O(N) 大小的额外空间。
    # 层序遍历 + 双端队列
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2: #通过res的长度来判断层数
                    tmp.appendleft(node.val)  # 偶数层 -> 队列头部
                else:
                    tmp.append(node.val)  # 奇数层 -> 队列尾部
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(list(tmp))
        return res

    #层序遍历 + 双端队列（奇偶层逻辑分离）
    #方法一代码简短、容易实现；但需要判断每个节点的所在层奇偶性，即冗余了 NN 次判断。
    #通过将奇偶层逻辑拆分，可以消除冗余的判断。
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, deque = [], collections.deque()
        deque.append(root)
        while deque:
            tmp = []
            # 打印奇数层
            for _ in range(len(deque)):
                # 从左向右打印
                node = deque.popleft()
                tmp.append(node.val)
                # 先左后右加入下层节点
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(tmp)
            if not deque: break  # 若为空则提前跳出
            # 打印偶数层
            tmp = []
            for _ in range(len(deque)):
                # 从右向左打印
                node = deque.pop()
                tmp.append(node.val)
                # 先右后左加入下层节点
                if node.right: deque.appendleft(node.right)
                if node.left: deque.appendleft(node.left)
            res.append(tmp)
        return res

    #层序遍历 + 倒序
    #此方法的优点是只用列表即可，无需其他数据结构。
    # 偶数层倒序： 若 res 的长度为 奇数 ，说明当前是偶数层，则对 tmp 执行 倒序 操作。
    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp[::-1] if len(res) % 2 else tmp)
        return res

