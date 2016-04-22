# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.getll(self.getnum(l1) + self.getnum(l2))

    def getnum(self, l):
        length = self.getlength(l)
        num = 0
        for i in range(length):
            num += l.val * (10 ** i)
            l = l.next
        return num

    def getll(self, num):
        nodelist = []
        while int(num/10):
            digit = num % 10
            num = int(num / 10)
            nodelist.append(ListNode(digit))

        nodelist.append(ListNode(num))     # add the last digit

        for i in range(len(nodelist) - 1):
            nodelist[i].next = nodelist[i + 1]

        return nodelist[0]

    def getlength(self, l):
        length = 1                # when linked list has just one node, length = 1, no loop
        while l.next is not None:
            length += 1
            l = l.next
        return length


if __name__ == '__main__':
    pass