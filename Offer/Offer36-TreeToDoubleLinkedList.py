class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #时间复杂度 O(N) ： N 为二叉树的节点数，中序遍历需要访问所有节点。
    #空间复杂度 O(N) ： 最差情况下，即树退化为链表时，递归深度达到 NN，系统使用 O(N) 栈空间。
    #采用后序递归遍历把cur节点和pre节点相连
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)  # 递归左子树
            if self.pre:  # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头节点
                self.head = cur
            self.pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        if not root:
            return
        self.pre = None #一开始设置为None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head #首位相连
        return self.head


