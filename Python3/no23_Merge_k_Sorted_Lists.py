# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def iter(lists):
            n = len(lists)
            if n == 1:
                return lists
            elif n == 2:
                return [self.mergeTwoLists(*lists)]
            elif n % 2 == 1:  # odd
                return iter(iter(lists[:int((n - 1) / 2)]) + iter(lists[int((n - 1) / 2):]))
            else:           # even
                return iter(iter(lists[:int(n / 2)]) + iter(lists[int(n / 2):]))
        return iter(lists)[0] if len(lists) != 0 else []

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        fifo = []
        p1, p2 = l1, l2
        while not (p1 is None and p2 is None):
            if p1 is None:
                fifo.append(p2)
                p2 = p2.next
            elif p2 is None:
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
            for index in range(len(fifo) - 1):
                fifo[index].next = fifo[index + 1]
            fifo[-1].next = None
            return fifo[0]
        else:
            return []

    # TLE solution:
    # def mergeKLists(self, lists):
    #     """
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """
    #     fifo = []
    #     pl = lists
    #     while self.removeNone(pl) != []:
    #         try:
    #             valuelist = [p.val for p in pl]
    #         except AttributeError:
    #             break
    #         minval = min(list(enumerate(valuelist)), key=lambda x: x[-1])
    #         minindex = minval[0]
    #         fifo.append(pl[minindex])
    #         pl[minindex] = pl[minindex].next

    #     if fifo != []:
    #         for index in range(len(fifo) - 1):
    #             fifo[index].next = fifo[index + 1]
    #         fifo[-1].next = None
    #         return fifo[0]
    #     else:
    #         return []

    # def removeNone(self, pl):
    #     for x in pl:
    #         if x == None:
    #             pl.remove(None)
    #     return pl
