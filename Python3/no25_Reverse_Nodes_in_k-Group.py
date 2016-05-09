# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        hasnewhead = False
        if head is None or k < 1:
            return head
        helper = head
        for _ in range(k): # length of linkedlist < k; k times test from 0 to k-1
            if helper is None:
                return head
            helper = helper.next

        while True:
            s = []
            for _ in range(k):
                s.append(head)
                head = head.next
            if not hasnewhead:
                newhead = s[-1]
                hasnewhead = True
            else:
                last.next = s[-1]
            last = s[0]
            for _ in range(k-1): # return listnodes in stack
                cur = s.pop()
                cur.next = s[-1]
            helper = head
            for _ in range(k):
                if helper is None:
                    last.next = head
                    return newhead
                else:
                    helper = helper.next
        #return newhead
