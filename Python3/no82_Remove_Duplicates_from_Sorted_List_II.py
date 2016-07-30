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
        newhead = ListNode(0)
        newhead.next = head
        pre = newhead
        p = head
        duplicate = False
        while p is not None:
            if p.next is not None and p.val == p.next.val:
                p.next = p.next.next
                duplicate = True
            elif duplicate:
                p = p.next
                pre.next = p
                duplicate = False
            else:
                pre = pre.next
                p = p.next
        return newhead.next


