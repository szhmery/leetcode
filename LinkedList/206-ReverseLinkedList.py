# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # https://www.bilibili.com/video/BV1g4411z7uN?from=search&seid=2204095547336912690
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        cur = head
        pre = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


    def reverseList2(self, head: ListNode) -> ListNode:
        new_head = None
        node = head
        last_node = head
        while node is not None:
            if node.next is None:
                if new_head is None:
                    # there is only one node in the list, just return this node
                    return node
                # this is the last node in the list
                node.next = last_node
                return new_head
            else:
                # move the head to the next node
                new_head = node.next

            if node == head:
                # this is the first node in the list
                node.next = None
            else:
                # point the node next to the last node, reverse the link
                node.next = last_node
            # for the next circle
            last_node = node
            node = new_head
        return new_head


if __name__ == '__main__':
    rawList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("\nBefore:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    solution = Solution()
    newList = solution.reverseList(rawList)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    rawList = ListNode(1)

    print("\nBefore:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    solution = Solution()
    newList = solution.reverseList(rawList)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
