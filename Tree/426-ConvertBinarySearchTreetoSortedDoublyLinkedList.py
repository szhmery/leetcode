class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # https://blog.csdn.net/zhangpeterx/article/details/89567460
    # https://www.cnblogs.com/grandyang/p/9615871.html
    # inorder iteration
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        dummy = Node()
        pre = dummy
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left = pre
            pre.right = node
            pre = node
            node = node.right
        dummy.right.left = pre
        pre.right = dummy.right
        return dummy.right

    # https://blog.csdn.net/zhangpeterx/article/details/89567460
    # recursion
    def treeToDoublyList2(self, root: 'Node') -> 'Node':
        def helper(node):
            nonlocal first, last
            if node:
                helper(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                helper(node.right)

        first, last = None, None
        helper(root)
        first.right = last
        last.left = first
        return first

    #https://www.cnblogs.com/grandyang/p/9615871.html
    # recursion, treeToDoublyList2 is better
    def treeToDoublyList3(self, root: 'Node') -> 'Node':
        def inorder(node, pre, head):
            if not node:
                return

            inorder(node.left, pre, head)
            if not head:
                head = node
                pre = node
            else:
                pre.right = node
                node.left = pre
                pre = node
            inorder(node.right, pre, head)

        if not root:
            return
        pre = None
        head = None
        inorder(root, pre=None, head=None)
        root.left = pre
        root.right = head
        return head
    # divide and conquer
    def treeToDoublyList4(self, root: 'Node') -> 'Node':
        def connect(node1, node2):
            if not node1:
                return node2
            if not node2:
                return node1
            tail1 = node1.left
            tail2 = node2.left
            tail1.right = node2
            node2.left = tail1
            tail2.right = node1
            node1.left = tail2
            return node1

        if not root:
            return
        left = self.treeToDoublyList4(root.left)
        right = self.treeToDoublyList4(root.right)
        root.left = root
        root.right = root
        return connect(connect(left, root), right)


