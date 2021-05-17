from Tree.PrintBST import PrintBST


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://www.bilibili.com/video/BV1ff4y197dS?from=search&seid=18183466807824298764
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        def findMid(head):
            slow = fast = head
            pre = None
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next

            pre.next = None
            return slow

        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        mid = findMid(head)
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root


if __name__ == '__main__':

    nums = ListNode(-10,ListNode(-3,ListNode(0, ListNode(5,ListNode(9)))))
    solution = Solution()
    bst = solution.sortedListToBST(nums)

    PrintBST.printBST(bst)
