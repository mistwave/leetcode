# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        fifo = []
        p1, p2 = l1, l2
        while not (p1 == None and p2 == None):
            if p1 == None:
                fifo.append(p2)
                p2 = p2.next
            elif p2 == None:
                fifo.append(p1)
                p1 = p1.next
            else:
                if p1.val < p2.val:
                    fifo.append(p1)
                    p1 = p1.next
                else:
                    fifo.append(p2)
                    p2 = p2.next
        if fifo != []:
            for index in range(len(fifo)-1):
                fifo[index].next = fifo[index + 1]
            fifo[-1].next = None
            return fifo[0]
        else:
            return []

