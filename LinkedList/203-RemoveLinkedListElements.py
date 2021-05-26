# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        dummy = ListNode()
        dummy.next = head
        cur = dummy

        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

if __name__ == '__main__':
    l1 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))

    solution = Solution()
    newList = solution.removeElements(l1, -1)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    l1 = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    solution = Solution()
    newList = solution.removeElements(l1, 7)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

