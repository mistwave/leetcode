class Solution(object):

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n % 4 == 0 else True


def test():
    s = Solution()
    for i in range(20):
        print('%d %s' % (i, s.canWinNim(i)))

if __name__ == '__main__':
    test()
