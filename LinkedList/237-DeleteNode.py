# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # https://www.bilibili.com/video/BV1vt4y1y7eM
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node:
            return

        # node_after = node.next
        node.val = node.next.val
        node.next = node.next.next
        # node_after.next = None


if __name__ == '__main__':
    rawList = ListNode(4)
    a = ListNode(5)
    rawList.next = a
    rawList.next.next = ListNode(1)
    rawList.next.next.next = ListNode(9)

    print("Before:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    solution = Solution()
    solution.deleteNode(a)
    print("\nAfter:")
    tmp_list = rawList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
