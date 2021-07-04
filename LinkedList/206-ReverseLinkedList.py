# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # recursive
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    # https://www.bilibili.com/video/BV1g4411z7uN?from=search&seid=2204095547336912690
    def reverseList2(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        cur = head
        pre = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


if __name__ == '__main__':
    rawList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("\nBefore:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    solution = Solution()
    newList = solution.reverseList(rawList)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    rawList = ListNode(1)

    print("\nBefore:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    solution = Solution()
    newList = solution.reverseList(rawList)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
