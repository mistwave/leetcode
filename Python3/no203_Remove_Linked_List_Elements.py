# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        newhead = ListNode(-val)
        newhead.next = head
        p = newhead
        while p.next is not None:
            if p.next.val != val:
                p = p.next
            else: # p.next.val == val
                if p.next.next is None: # p.next is the last node
                    p.next = None
                else: # not the last node
                    p.next = p.next.next
        return newhead.next
