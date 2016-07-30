# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        p1, p2 = head, head

        while p1.next is not None and p2.next is not None:
            p1, p2 = p1.next, p2.next
            if p2.next is not None:
                p2 = p2.next
            else:
                break
            if p1 is p2:
                p2 = head
                while True:
                    if p1 is p2:
                        return p1
                    p1, p2 = p1.next, p2.next
        return None

