# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        # find the mid point
        p1, p2 = head, head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        # reverse right part
        first, reverse = p1.next, None
        while first:
            second = first.next
            first.next = reverse
            reverse = first
            first = second
        left, right = head, reverse
        while right and right.val == left.val:
            left, right = left.next, right.next
        return right is None

