# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        # find the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p1 = head
        # reverse the list between middle node and end node
        p2 = self.reserve(slow)
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True

    def reserve(self, head):
        if head is None or head.next is None:
            return head
        cur = head
        pre = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def isPalindrome2(self, head: ListNode) -> bool:
        p1 = head
        p2 = head
        res = True
        while p2.next is not None and p2.next.next is not None:
            p1 = p1.next
            p2 = p2.next.next
            continue

        middle = p1
        precurrent = p1.next
        if precurrent is None:
            # only one node in the list
            return True
        while precurrent.next is not None:
            current = precurrent.next
            precurrent.next = current.next
            current.next = middle.next
            middle.next = current

        p1 = head
        p2 = middle.next
        while p1 is not middle:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                res = False
                break
        if p1 == middle:
            if p2 is not None and p1.val != p2.val:
                return False
        return res

    def isPalindrome3(self, head: ListNode) -> bool:
        node = head
        value_list = []
        # get all of values and save them to a list
        while node is not None:
            value_list.append(node.val)
            node = node.next

        for i in range(len(value_list) // 2):
            if value_list[i] != value_list[len(value_list) - 1 - i]:
                return False
        return True


if __name__ == '__main__':
    rawList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("\nBefore:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    solution = Solution()
    result = solution.isPalindrome(rawList)
    print("\nMethod 1: Is palindrome:", end=' ')
    print(result)

    result = solution.isPalindrome2(rawList)
    print("\nMethod 2: Is palindrome:", end=' ')
    print(result)

    rawList1 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))

    print("\nBefore:")
    tmp_list = rawList1
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    solution = Solution()
    result = solution.isPalindrome(rawList1)
    print("\nMethod 1: Is palindrome:", end=' ')
    print(result)

    result = solution.isPalindrome2(rawList1)
    print("\nMethod 2: Is palindrome:", end=' ')
    print(result)

    rawList2 = ListNode(1, ListNode(0, ListNode(3, ListNode(4, ListNode(0, ListNode(1))))))
    print("\nBefore:")
    tmp_list = rawList2
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
    result = solution.isPalindrome(rawList2)
    print("\nMethod 1: Is palindrome:", end=' ')
    print(result)
    result = solution.isPalindrome2(rawList2)
    print("\nMethod 2: Is palindrome:", end=' ')
    print(result)
    result = solution.isPalindrome3(rawList2)
    print("\nMethod 3: Is palindrome:", end=' ')
    print(result)
    rawList3 = ListNode(1)
    print("\nBefore:")
    tmp_list = rawList3
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
    result = solution.isPalindrome(rawList3)
    print("\nMethod 1: Is palindrome:", end=' ')
    print(result)

    result = solution.isPalindrome2(rawList3)
    print("\nMethod 2: Is palindrome:", end=' ')
    print(result)