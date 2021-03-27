class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # find which list is head
        if l1.val <= l2.val:
            head = l1
        else:
            head = l2
        # the left list is used to insert to head
        if head is l1:
            insert_list = l2
        else:
            insert_list = l1

        node = head
        if node.next is not None:
            # get the next node
            next_node = node.next
        else:
            # if the inserted list has only one node
            head.next = insert_list
            return head

        insert_node = insert_list

        while insert_list is not None:
            if node.val <= insert_node.val <= next_node.val:
                # need to insert insert_node after node and before next_node
                insert_list = insert_node.next
                node.next = insert_node
                insert_node.next = next_node
                # for the next circle, move node to insert_node, next_node doesn't move, get next insert_node
                node = insert_node
                insert_node = insert_list
            else:
                # find the next inserted point, move node to the next_node, next_node move to the next one
                node = next_node
                next_node = node.next

            if next_node is None:
                # if inserted list is empty, just insert insert_list to end
                node.next = insert_list
                return head
        return head


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l2 = ListNode(1, ListNode(4, ListNode(4, ListNode(5, ListNode(10)))))

    solution = Solution()
    newList = solution.mergeTwoLists(l1, l2)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list != None:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
