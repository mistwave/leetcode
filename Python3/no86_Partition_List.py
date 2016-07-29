# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        newhead = ListNode(-1)
        newhead.next = head
        pre = newhead
        precur = newhead
        cur = head
        while cur is not None:
            if cur.val >= x:
                cur, precur = cur.next, precur.next
            else:  # cur.val < x
                if pre.next is cur:
                    pre, cur, precur = pre.next, cur.next, precur.next
                else:  # pre.next is not cur, need to be replaced
                    # change the order
                    precur.next = cur.next
                    cur.next = pre.next
                    pre.next = cur
                    # continue the iteration
                    pre = pre.next
                    cur = precur.next
        return newhead.next
