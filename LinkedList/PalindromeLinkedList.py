# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
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

if __name__ == '__main__':
    rawList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("\nBefore:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    solution = Solution()
    result = solution.isPalindrome(rawList)
    print("\nIs palindrome:", end=' ')
    print(result)

    rawList1 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    rawList2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
    rawList3 = ListNode(1)

    print("\nBefore:")
    tmp_list = rawList1
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    solution = Solution()
    result = solution.isPalindrome(rawList1)
    print("\nIs palindrome:", end=' ')
    print(result)

    result = solution.isPalindrome2(rawList1)
    print("\nIs palindrome:", end=' ')
    print(result)

    print("\nBefore:")
    tmp_list = rawList3
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
    result = solution.isPalindrome2(rawList3)
    print("\nIs palindrome:", end=' ')
    print(result)