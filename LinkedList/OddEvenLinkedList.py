# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head

        odd_head = odd = head
        even_head = even = odd_head.next
        curr = even_head.next

        while curr is not None:
            odd.next = curr
            if curr.next:
                even.next = curr.next
            else:
                even.next = None
                odd = odd.next
                break
            odd = odd.next
            even = even.next
            curr = even.next
        odd.next = even_head
        return odd_head

    #   Complexity Analysis
    # Time complexity : O(n). There are total nn nodes and we visit each node once.
    # Space complexity : O(1). All we need is the four pointers.
    def oddEvenList2(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        odd = head
        even_head = even = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    newList = solution.oddEvenList2(l1)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    newList = solution.oddEvenList2(l2)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
