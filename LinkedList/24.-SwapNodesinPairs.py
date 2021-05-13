# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # iterate
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode()
        dummy.next = head
        first = head
        second = head.next
        pre = dummy
        while first and second:
            if second.next:
                tmp_first = second.next
                tmp_second = second.next.next if second.next.next else None
            else:
                tmp_first = None
                tmp_second = None
            first.next = second.next
            second.next = first
            pre.next = second
            pre = first
            first = tmp_first
            second = tmp_second
        return dummy.next

    # recursive
    def swapPairs2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        t = head.next
        head.next = self.swapPairs2(head.next.next)
        t.next = head
        return t

if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    solution = Solution()
    newList = solution.swapPairs(l1)
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