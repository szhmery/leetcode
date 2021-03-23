# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp_list = head
        length = 0
        while tmp_list != None:
            length += 1
            tmp_list = tmp_list.next
        if length == 1 and n == 1:
            return None
        tmp_list = head
        before_node = head
        index = 0
        while tmp_list != None:
            index += 1
            if index == length - n + 1:
                if before_node == head and tmp_list == head:
                    head = tmp_list.next
                    return head
                before_node.next = tmp_list.next
                tmp_list = None
            else:
                before_node = tmp_list
                tmp_list = tmp_list.next
        return head


if __name__ == '__main__':
    rawList = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

    print("\nBefore:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    solution = Solution()
    rawList = solution.removeNthFromEnd(rawList, 2)
    print("\nAfter:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    rawList = ListNode(1, ListNode(2))
    print("\nBefore:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    solution = Solution()
    rawList = solution.removeNthFromEnd(rawList, 2)
    print("\nAfter:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next