# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


if __name__ == '__main__':
    l1 = ListNode(-1, ListNode(-1, ListNode(3, ListNode(4, ListNode(4)))))

    solution = Solution()
    newList = solution.deleteDuplicates(l1)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next