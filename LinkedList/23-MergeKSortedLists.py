from typing import List
from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        # python3 不允许插入优先级相同的值或者是无法判断优先级的值到优先队列。
        # 刷题看到一种不错的方法，插入的时候加入一个index,就不会出现优先级相同的情况了。
        for index, l in enumerate(lists):
            if l:
                q.put((l.val, index, l))
        while not q.empty():
            val, index, node = q.get()
            point.next = node
            point = point.next
            node = node.next
            if node:
                q.put((node.val, index, node))

        return head.next

    # Merge with Divide And Conquer
    # time complexity O(Nlogk)
    # space complexity O(1)
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        def merge2Lists(l1, l2):
            curr = dummp = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            curr.next = l1 or l2
            return dummp.next
        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if n > 0 else None

    #  Merge lists one by one, DON'T choose this one
    # time complexity O(Nk)
    # space complexity O(1)
    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:
        def merge2Lists(l1, l2):
            curr = dummp = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            curr.next = l1 or l2
            return dummp.next

        if not lists:
            return None
        for i in range(len(lists) - 1):
            lists[0] = merge2Lists(lists[0], lists[i + 1])
        return lists[0]


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    lists = [l1, l2, l3]
    newList = solution.mergeKLists(lists)
    print("\nAfter method 1 :")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    lists = [l1, l2, l3]
    newList = solution.mergeKLists2(lists)
    print("\nAfter method 2 :")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next