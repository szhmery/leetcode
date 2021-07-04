"""
# Definition for a Node.
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # https://www.bilibili.com/video/BV1UA411J775?from=search&seid=5592627129777324069
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        node_map = {}
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next is None:
                node_map[curr].next = None
            else:
                node_map[curr].next = node_map[curr.next]
            if curr.random is None:
                node_map[curr].random = None
            else:
                node_map[curr].random = node_map[curr.random]
            curr = curr.next
        return node_map[head]

    # https://www.bilibili.com/video/BV1BN411R7a8?from=search&seid=5592627129777324069
    # recursive
    def __init__(self):
        self.visit = {None: None}

    def copyRandomList2(self, head: 'Node') -> 'Node':
        if head in self.visit:
            head = self.visit[head]
        if not head:
            return
        node = Node(head.val)
        self.visit[head] = node
        node.next = self.copyRandomList2(head.next)
        node.random = self.copyRandomList2(head.random)
        return node


if __name__ == '__main__':
    l = Node(1)
    a = Node(2)
    l.next = a
    l.random = a
    a.random = a

    solution = Solution()
    newList = solution.copyRandomList2(l)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
