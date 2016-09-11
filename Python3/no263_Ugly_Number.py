class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for fac in (2, 3, 5):
            while num and num % fac == 0: # rule out 0
                num = num // fac
        return num == 1
