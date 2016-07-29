# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        cur = head
        # transform 1 -> 2 -> 3 -> None into:
        # 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> None
        while cur is not None:
            new = RandomListNode(cur.label)

            new.next = cur.next
            cur.next = new
            cur = new.next

        # adjust n'-node's random value
        cur = head
        while cur is not None:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # return copy (put n' into 1 linked list)

        newhead = head.next
        old, new = head, newhead
        while new.next is not None:
            old.next = new.next
            old = old.next
            new.next = old.next
            new = new.next
        new.next = old.next = None
        return newhead
