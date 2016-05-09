# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # my slow solution
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hasnewhead = False
        if head is None or head.next is None: # length of linked list is 0 or 1 (< 2)
            return head
        while True:
            s = []
            for _ in range(2):
                s.append(head)
                head = head.next
            if not hasnewhead:
                newhead = s[-1]
                hasnewhead = True
            else:
                last.next = s[-1]
            last = s[0]
            s[-1].next = s[0]
            if head is None or head.next is None:
                last.next = head
                break

        return newhead


