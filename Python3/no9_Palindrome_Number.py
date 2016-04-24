import math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0:
            return False
        n = int(math.log10(abs(x)))
        base = 10 ** n

        while x:
            if not int(x / base) == x % 10:
                return False
            x = int((x % base) / 10)
            base /= 100
        return True


if __name__ == '__main__':
    testlist = [-1,0,1,123321,1234567,12321]
    s = Solution()
    for num in testlist:
        print('{0}: {1}'.format(num,s.isPalindrome(num)))

