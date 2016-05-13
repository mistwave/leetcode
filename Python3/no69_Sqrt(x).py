class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if x == 0 or x == 1:
            return x
        left, right = 0, x
        while left + 1 != right:
            tmp = int(left + (right - left)/2)
            tmp2 = tmp**2
            if tmp2 == x:
                return tmp
            elif tmp2 > x:
                right = tmp
            else: # tmp2 < x:
                left = tmp

        return left


def test():
    s = Solution()
    for i in range(10):
        print("sqrt({0}): {1}".format(10**i, s.mySqrt(10**i)))


if __name__ == '__main__':
    test()
