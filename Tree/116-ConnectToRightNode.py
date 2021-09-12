from Tree.PrintBST import PrintBST
"""
# Definition for a Node.
Answer: https://segmentfault.com/a/1190000003465911
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # Breadth first search - BFS
    # space O(n)
    # time O(n)
    # 时间复杂度：O(N)。每个节点会被访问一次且只会被访问一次，即从队列中弹出，并建立 next 指针。
    # 空间复杂度：O(N)。这是一棵完美二叉树，它的最后一个层级包含 N/2 个节点。广度优先遍历的复杂度取决于一个层级上的最大元素数量。
    # 这种情况下空间复杂度为 O(N)。
    def connect(self, root: 'Node') -> 'Node':
        queue = []
        if root is None:
            return None
        queue.append(root)
        while len(queue) != 0:
            size = len(queue)

            for i in range(size):
                first = queue[0]
                queue.remove(first)
                if i < size - 1:
                    first.next = queue[0]
                if first.left:
                    queue.append(first.left)
                if first.right:
                    queue.append(first.right)
        return root

    # recursive
    # space O(n)
    # time O(n)
    def connect2(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        if root.left:
            root.left.next = root.right
        if root.right:
            root.right.next = root.next.left if root.next else None
        self.connect2(root.left)
        self.connect2(root.right)
        return root

    # two pointers
    # space O(n)
    # time O(1)
    def connect3(self, root: 'Node') -> 'Node':
        if root is None:
            return
        p = root
        first = None
        while p:
            if first is None:
                first = p.left
            if p.left:
                p.left.next = p.right
            else:
                # this layer is finished.
                break
            if p.next:
                p.right.next = p.next.left
                p = p.next
            else:
                p = first
                first = None
        return root

    # Hierarchical progressive method
    # space O(n)
    # time O(1)
    # 时间复杂度：O(N)，每个节点只访问一次。
    # 空间复杂度：O(1)，不需要存储额外的节点。
    def connect4(self, root: 'Node') -> 'Node':
        head = root
        while head:
            tmp_head = head
            while head:
                if head.left:
                    head.left.next = head.right
                if head.right:
                    head.right.next = head.next.left if head.next else None
                head = head.next
            head = tmp_head.left
        return root

    def connect5(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            tmp = queue
            queue = []
            pre = None
            while tmp:
                node = tmp.pop(0)
                if node.right and node.left:
                    node.right.next = pre
                    node.left.next = node.right
                    pre = node.left
                    queue.append(node.right)
                    queue.append(node.left)
        return root

if __name__ == '__main__':
    root = Node(1)
    a = Node(2)
    b = Node(3)
    root.left = a
    root.right = b
    a.left = Node(4)
    a.right = Node(5)
    b.left = Node(6)
    b.right = Node(7)
    a.left.left = Node(8)
    a.left.right = Node(9)
    a.right.left = Node(10)
    a.right.right = Node(11)
    b.left.left = Node(12)
    b.left.right = Node(13)
    b.right.right = Node(14)
    b.right.right = Node(15)

    solution = Solution()
    root = solution.connect(root)
    print('method 1: connect:')
    PrintBST.printBST(root)
    root = solution.connect2(root)
    print('method 2: connect:')
    PrintBST.printBST(root)
    root = solution.connect3(root)
    print('method 3: connect:')
    PrintBST.printBST(root)
    root = solution.connect5(root)
    print('method 5: connect:')
    PrintBST.printBST(root)