# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        p = head
        while p.next is not None:
            if p.val == p.next.val:
                p.next = p.next.next # delete p.next
            else:
                p = p.next
        return head
