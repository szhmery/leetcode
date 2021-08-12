from Tree.PrintBST import PrintBST
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # DFS
    #https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/solution/jian-zhi-offer-26-shu-de-zi-jie-gou-die-0qjeh/
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def compare(a, b):
            if not b:
                return True
            if not a or a.val != b.val:
                return False
            return compare(a.left, b.left) and compare(a.right, b.right)
        if not B:
            return False
        if not A:
            return False
        if A.val == B.val:
            if compare(A, B):
                return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    # preorder and DFS
    def isSubStructure2(self, A: TreeNode, B: TreeNode) -> bool:
        def isSameTree(a: TreeNode, b: TreeNode):
            if not b:
                return True
            if a and b and a.val == b.val:
                return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
            else:
                return False

        if not B:
            return False
        stack = []
        node = A
        while node or stack:
            while node:
                if node.val == B.val:
                    if isSameTree(node, B):
                        return True
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return False

    # BFS
    #https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/solution/jian-zhi-offer-26-shu-de-zi-jie-gou-die-0qjeh/
    def isSubStructure3(self, A: TreeNode, B: TreeNode) -> bool:
        def bfs(A, B):
            queue = [(A, B)]
            while queue:
                nodeA, nodeB = queue.pop(0)
                if not nodeA or nodeA.val != nodeB.val:
                    return False
                if nodeB.left:
                    queue.append((nodeA.left, nodeB.left))
                if nodeB.right:
                    queue.append((nodeA.right, nodeB.right))
            return True
        if not B:
            return False
        q = [A]
        while q:
            node = q.pop(0)
            if node.val == B.val:
                if bfs(node, B):
                    return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False