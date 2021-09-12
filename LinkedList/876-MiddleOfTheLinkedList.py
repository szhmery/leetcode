from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #时间复杂度：O(N)，其中 N 是给定链表的结点数目。
    #空间复杂度：O(1)，只需要常数空间存放 slow 和 fast 两个指针
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
