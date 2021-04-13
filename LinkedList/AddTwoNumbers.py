# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Complexity Analysis
    # Time complexity : O(max(m,n)). Assume that mm and nn represents the length of l1 and l2 respectively,
    # the algorithm above iterates at most max(m,n) times.
    # Space complexity : O(max(m,n)). The length of the new list is at most \max(m,n) + 1ma
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        l3 = dummy
        overbit = 0
        while l1 is not None or l2 is not None:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum_val = x + y + overbit
            l3.next = ListNode(sum_val % 10)
            overbit = int(sum_val / 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l3 = l3.next
        if overbit > 0:
            l3.next = ListNode(1)
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))

    solution = Solution()
    newList = solution.addTwoNumbers(l1, l2)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
