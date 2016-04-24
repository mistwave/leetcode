import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        flag = 1 if x > 0 else -1
        x = abs(x)
        num = 0
        for i in range(1 + int(math.log10(x))):
            digit = x % 10
            x = int(x / 10)
            num = num*10 + digit

        num *= flag
        if num < MIN_INT or num > MAX_INT:
            return 0
        else:
            return num

if __name__ == '__main__':
    testlist = [123,-213,1000000,10000000003]
    s = Solution()
    for num in testlist:
        print("{0}: {1}".format(num, s.reverse(num)))
