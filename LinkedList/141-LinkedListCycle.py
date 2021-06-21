# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = slow.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        if not head:
            return False
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False


if __name__ == '__main__':
    rawList = ListNode(1)
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(3)

    rawList.next = a
    a.next = b
    b.next = c
    c.next = a

    solution = Solution()
    result = solution.hasCycle(rawList)
    print("\nmethod 1 Has cycle:", end=' ')
    print(result)
    result = solution.hasCycle2(rawList)
    print("\nmethod 2 Has cycle:", end=' ')
    print(result)

    rawList = ListNode(1)
    a = ListNode(3)
    b = ListNode(2)

    rawList.next = a
    a.next = b
    b.next = rawList

    solution = Solution()
    print("\nmethod 1 Has cycle:", end=' ')
    print(result)
    result = solution.hasCycle2(rawList)
    print("\nmethod 2 Has cycle:", end=' ')
    print(result)
