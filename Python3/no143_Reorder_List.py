# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # # recursive: TLE
        # # 01 -> 01; 012 -> 021; len <= 2 return head
        # def iter(head):
        #     if head is None or head.next is None or head.next.next is None:
        #         return head
        #     # 0123456 -> 06[12345] -> 06[15[234]] -> 06[15[24[3]]] / 0615243
        #     dummy = ListNode(-1)
        #     dummy.next = head
        #     pre = last = head
        #     while last.next is not None:
        #         dummy, last = dummy.next, last.next
        #     dummy.next = None
        #     last.next = pre.next
        #     pre.next = last
        #     last.next = iter(last.next)
        #     return head
        # head = iter(head)
        s = []
        while head:
            s.append(head)
            head = head.next
        cnt = -1
        for i in range(len(s)):
            # 0   1  2   3   4  5  -> 0 5 1 4 2 3
            # -1 -2 -3 None -4 -5  <-- nextindex; s[i].next = s[nextindex] except s[len//2].next = None
            if i == len(s) // 2:
                s[i].next = None
            else:
                s[i].next = s[cnt]
                cnt -= 1
