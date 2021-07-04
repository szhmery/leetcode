class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # https://leetcode.com/problems/reverse-linked-list-ii/solution/
    def reverseBetween_recursion(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return head
        l_node, r_node = head, head
        stop = False

        def recursion(r_node, m, n):
            nonlocal l_node, stop
            if n == 1:
                return
            r_node = r_node.next
            if m > 1:
                l_node = l_node.next
            recursion(r_node, m - 1, n - 1)
            if l_node == r_node or r_node.next == l_node:
                stop = True
            if not stop:
                l_node.val, r_node.val = r_node.val, l_node.val
                l_node = l_node.next

        recursion(r_node, left, right)
        return head


    #https://leetcode.com/problems/reverse-linked-list-ii/solution/
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head

    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        cur = 0
        pre = dummy
        while head:
            cur += 1
            if cur == left:
                o_pre = pre
                end = head
                while cur != right + 1 and head:
                    next = head.next
                    head.next = pre
                    pre = head
                    head = next
                    cur += 1

                o_pre.next = pre
                end.next = head
                break
            else:
                pre = head
                head = head.next
        return dummy.next

class Solution2:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head

if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("\nBefore:")
    tmp_list = l1
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution = Solution()
    newList = solution.reverseBetween_recursion(l1, 2, 4)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

