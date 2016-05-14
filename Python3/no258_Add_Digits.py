class Solution(object):
    # solution 1:

    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            tmp = 0
            while num != 0:
                tmp += num % 10
                num = int(num / 10)
            num = tmp
        return num

    # solution 2:
    # 717865: 7+1=8 8+7=15-->1+5=6 6+8=14-->5 5+6=11-->2 2+5 = 7
    # and vice versa
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = 0
        a = num % 10
        num = int(num / 10)
        b = 0
        while num != 0:
            b = num % 10
            num = int(num / 10)
            tmp = a + b
            if tmp >= 10:
                tmp = tmp % 10 + int(tmp / 10)
            a = tmp
        return a

    def addDigits3(self, num):
        return num if num == 0 else num % 9 or 9


def test():
    s = Solution()
    print(s.addDigits(5434234234))
    print(s.addDigits1(5434234234))
if __name__ == '__main__':
    test()
