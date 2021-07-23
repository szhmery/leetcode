# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def helper(node1: TreeNode, node2: TreeNode):
            # 如果node1后面还跟着多余的节点，认为是False，必须同为末节点
            # 如果可以带多余节点，那么只需要node2为null即返回True
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and helper(node1.left, node2.left) and helper(node1.right, node2.right)

        if not root:
            return False
        if helper(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


solution = Solution()
Tree1 = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
Tree1.left = a
Tree1.right = b
a.left = TreeNode(4)
Tree2 = TreeNode(2)
Tree2.left = TreeNode(4)
print(solution.isSubtree(Tree1, Tree2))

# 比Tree2多了一个末节点，返回False
Tree1 = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(4)
Tree1.left = a
Tree1.right = b
a.left = c
c.left = TreeNode(5)

Tree2 = TreeNode(2)
Tree2.left = TreeNode(4)
print(solution.isSubtree(Tree1, Tree2))
