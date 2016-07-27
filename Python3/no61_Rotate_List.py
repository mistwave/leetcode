# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def getlen(head):
            if head is None:
                return 0
            tmp = head
            cnt = 1
            while tmp.next is not None:
                cnt += 1
                tmp = tmp.next
            return cnt
         
        if head is None or head.next is None or k == 0:
            return head
        k = k % getlen(head)     
        if k == 0:
            return head
        
        p, q = head, head
        for i in range(k):
            if q.next is not None:  # k == len(linkedlist) situation (reverse the linked list)
                q = q.next
        while q.next is not None:
            p, q = p.next, q.next
        newhead = p.next
        q.next = head
        p.next = None
        return newhead
        