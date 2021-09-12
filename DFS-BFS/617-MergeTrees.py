# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # DFS
    # 时间复杂度：O(min(m,n))，其中 m 和 n 分别是两个二叉树的节点个数。对两个二叉树同时进行深度优先搜索，
    # 只有当两个二叉树中的对应节点都不为空时才会对该节点进行显性合并操作，因此被访问到的节点数不会超过较小的二叉树的节点数。
    # 空间复杂度：O(min(m,n))，其中 m 和 n 分别是两个二叉树的节点个数。
    # 空间复杂度取决于递归调用的层数，递归调用的层数不会超过较小的二叉树的最大高度，最坏情况下，二叉树的高度等于节点数。
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root
    # BFS
    # 时间复杂度：O(min(m,n))，其中 m 和 n 分别是两个二叉树的节点个数。对两个二叉树同时进行深度优先搜索，
    # 只有当两个二叉树中的对应节点都不为空时才会对该节点进行显性合并操作，因此被访问到的节点数不会超过较小的二叉树的节点数。
    # 空间复杂度：O(N)，对于满二叉树时，要保存所有的叶子节点，即 N/2 个节点。
    def mergeTrees2(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        queue = [(root1, root2)]
        while queue:
            r1, r2 = queue.pop()
            r1.val += r2.val
            # 如果r1和r2的左子树都不为空，就放到队列中
            # 如果r1的左子树为空，就把r2的左子树挂到r1的左子树上
            if r1.left and r2.left:
                queue.append((r1.left, r2.left))
            elif not r1.left:
                r1.left = r2.left
            if r1.right and r2.right:
                queue.append((r1.right, r2.right))
            elif not r1.right:
                r1.right = r2.right
        return root1

