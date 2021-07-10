# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        pre = None
        while stack1 or stack2 or carry:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            value = v1 + v2 + carry
            new = ListNode(value % 10)
            new.next = pre
            pre = new
            carry = value // 10

        return new


if __name__ == '__main__':
    l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(6, ListNode(1)))))
    l2 = ListNode(1, ListNode(1, ListNode(5, ListNode(6, ListNode(4)))))

    solution = Solution()
    newList = solution.addTwoNumbers(l1, l2)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
