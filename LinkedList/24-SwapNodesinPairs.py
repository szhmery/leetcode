# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # recursive
    def swapPairs2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        t = head.next
        head.next = self.swapPairs2(head.next.next)
        t.next = head
        return t

    # iterate
    # https://www.bilibili.com/video/BV1ih411f7YK?from=search&seid=9650532595680486726
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode()
        dummy.next = head
        res = dummy
        while dummy.next and dummy.next.next:
            first = dummy.next
            second = dummy.next.next
            first.next = second.next
            second.next = first
            dummy.next = second
            dummy = dummy.next.next
        return res.next


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    solution = Solution()
    newList = solution.swapPairs2(l1)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    newList = solution.swapPairs(l1)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    l1 = ListNode(1, ListNode(2))

    newList = solution.swapPairs(l1)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
    l1 = ListNode(1, ListNode(2))

    newList = solution.swapPairs2(l1)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next