# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #iteration
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node

    # recursion
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor2(root.right, p, q)
        if root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor2(root.left, p, q)
        return root

    # use addtional dict
    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not p or not q:
            return root
        def getPath(root, target):
            parent_path = []
            node = root
            while node.val != target.val:
                parent_path.append(node.val)
                if node.val > target.val:
                    node = node.left
                else:
                    node = node.right
            return
        parent = None
        p_path = getPath(root, p)
        q_path = getPath(root, q)
        for u, v in zip(p_path, q_path):
            if u == v:
                parent = v
            else:
                break
        return parent
