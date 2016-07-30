# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        p1, p2 = head, head
        while p1.next is not None and p2.next is not None:
            p1, p2 = p1.next, p2.next
            if p2.next is not None:
                p2 = p2.next
            else:
                break
            if p1 == p2:
                return True

        return False

