# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        newhead = ListNode(-1)
        newhead.next = head
        p = newhead
        while p is not None:
            # 1 ≤ m ≤ n ≤ length of list.
            # devide into: ... -> pre -> p1 -> ... -> p2 -> last -> ...
            # reverse from p1 to p2
            # return ... -> pre -> reverse(p1 -> ... -> p2) -> last -> ...
            if m == 1:
                pre = p
            if m == 0:
                p1 = p
            if n == 0:
                p2, last = p, p.next
                break
            p = p.next
            m, n = m - 1, n - 1

        first, reverse = p1, None
        while first is not last:
            second = first.next
            first.next = reverse
            reverse = first
            first = second
        # combine together: ... pre [reversed] last ...
        pre.next = reverse
        p1.next = last

        return newhead.next
