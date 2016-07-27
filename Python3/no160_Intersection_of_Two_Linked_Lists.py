# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pa, pb = headA, headB
        cnta, cntb = 1, 1
        while pa.next is not None:
            pa = pa.next
            cnta += 1
        while pb.next is not None:
            pb = pb.next
            cntb += 1
        if pa is not pb:
            return None
        else:
            pa, pb = headA, headB
            for i in range(abs(cnta-cntb)):
                if cnta < cntb:
                    pb = pb.next
                elif cnta > cntb:
                    pa = pa.next
            while True:
                if pa is pb:
                    return pa
                else:
                    pa, pb = pa.next, pb.next


