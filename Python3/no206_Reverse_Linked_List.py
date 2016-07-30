# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # recursive solution
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        second = head.next
        rest = self.reverseList(second)
        second.next = head
        head.next = None
        return rest


    # iterative solution
    def reverseList_fast(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        reverse = None
        first = head
        while first is not None:
            second = first.next
            first.next = reverse
            reverse = first
            first = second
        return reverse
