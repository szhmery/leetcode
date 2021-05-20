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
    root = solution.connect4(root)
    print('method 4: connect:')
    PrintBST.printBST(root)