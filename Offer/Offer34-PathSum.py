from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 时间复杂度 O(N) ： N 为二叉树的节点数，先序遍历需要遍历所有节点。
    # 空间复杂度 O(N) ： 最差情况下，即树退化为链表时，path 存储所有树节点，使用 O(N) 额外空间。
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        def recur(root, tar):
            if not root:
                return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right: #tar为0，左右子树都是空才记录
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop() # 记得弹出，回溯。

        recur(root, sum)
        return res

