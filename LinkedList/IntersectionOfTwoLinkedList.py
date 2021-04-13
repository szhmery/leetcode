# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Complexity Analysis
    # Let NN be the length of list A and MM be the length of list B.
    # Time complexity : O(N×M).
    # For each of the N nodes in list A, we are traversing over each of the nodes in list B. In the worst case,
    # we won't find a match, and so will need to do this until reaching the end of list B, giving a worst-case time
    # complexity of O(N×M).
    # Space complexity : O(1)
    # We aren't allocating any additional data structures, so the amount of extra space used does not grow with the size
    # of the input.
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA = headA
        currB = headB
        while currA:
            while currB:
                if currA is currB:
                    return currA
                else:
                    currB = currB.next
            currB = headB
            currA = currA.next
        return None

    # Complexity Analysis
    # Time complexity : O(N + M).
    # Firstly, we need to build up the hash table. It costs O(1) to insert an item into a hash table, and we need to do
    # this for each of the M nodes in list B. This gives a cost of O(M) for building the hash table.
    # Secondly, we need to traverse list A, and for each node, we need to check whether or not it is in the hash table.
    # In the worst case, there will not be a match, requiring us to check all N nodes in list A. As it is also O(1) to
    # check whether or not an item is in a hash table, this checking has a total cost of O(N).
    # Finally, combining the two parts, we get O(M) + O(N) =O(M+N).

    # Space complexity : O(M).
    # As we are storing each of the nodes from list B into a hash table, the hash table will require O(M) space.
    # Note that we could have instead stored the nodes of list A into the hash table, this would have been a space
    # complexity of O(N). Unless we know which list is longer though, it doesn't make any real difference.
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        dict_B = set()
        while headB:
            dict_B.add(headB)
            headB = headB.next
        while headA:
            if headA in dict_B:
                return headA
            headA = headA.next
        return None


if __name__ == '__main__':
    solution = Solution()
    headA = ListNode(1)
    a = ListNode(2)
    a.next = ListNode(4)
    headB = ListNode(3)

    headA.next = a
    headB.next = a
    print("\nbefore:")
    tmp_list = headA
    while tmp_list:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next

    newList = solution.getIntersectionNode2(headA, headB)
    print("\nAfter:")
    tmp_list = newList
    while tmp_list:
        print(str(tmp_list.val), end='->')
        tmp_list = tmp_list.next
