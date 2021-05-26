# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # https://www.bilibili.com/video/BV1jK411N7e6
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        n = 1
        tail = head
        while head.next:
            head = head.next
            n += 1
        head.next = tail # connect the tail to head
        head = head.next # get the head again
        k %= n
        for i in range(n - k - 1):
            head = head.next
        res = head.next
        head.next = None
        return res


if __name__ == '__main__':
    l1 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))

    solution = Solution()
    newList = solution.rotateRight(l1, 2)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

