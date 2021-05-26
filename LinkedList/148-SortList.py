# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # https://www.bilibili.com/video/BV1VK411A7Gm
    # (n logn) time and O(1) memory
    def merge(self, h1, h2):
        dummy = tail = ListNode()
        while h1 and h2:
            if h1.val < h2.val:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            tail = tail.next
        tail.next = h1 or h2
        return dummy.next

    # fast and slow pointer
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = None
        slow = head
        fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))


if __name__ == '__main__':
    l1 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))

    solution = Solution()
    newList = solution.sortList(l1)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
    l1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))

    newList = solution.sortList(l1)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next