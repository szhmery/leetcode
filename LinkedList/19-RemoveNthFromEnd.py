# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # one pass algorithm
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        if not head or n == 0:
            return
        dummy = ListNode()
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n + 1):
            if not first.next:
                return
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

    # two pass algorithm
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = head
        length = 0
        while first:
            length += 1
            first = first.next
        length -= n
        first = dummy
        while length > 0:
            first = first.next
            length -= 1
        first.next = first.next.next
        return dummy.next




if __name__ == '__main__':
    rawList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("\nBefore:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    solution = Solution()
    rawList = solution.removeNthFromEnd(rawList, 2)
    print("\nAfter:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    rawList = ListNode(1, ListNode(2))
    print("\nBefore:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    rawList = solution.removeNthFromEnd2(rawList, 2)
    print("\nAfter:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    rawList = ListNode(1)
    rawList = solution.removeNthFromEnd2(rawList, 1)
    print("\nAfter:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    rawList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    rawList = solution.removeNthFromEnd2(rawList, 2)
    print("\nMethod 3 After:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
    rawList = ListNode(1)
    rawList = solution.removeNthFromEnd2(rawList, 1)
    print("\nMethod 3 After:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
