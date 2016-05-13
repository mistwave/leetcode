class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 0:
            return 0
        elif n > 0:
            if n == 1:
                return x
            elif n % 2 == 0:
                return self.myPow(x * x, n / 2)
            elif n % 2 == 1:
                return x * self.myPow(x, n - 1)
            else:
                return None
        else:  # n < 0
            return 1 / self.myPow(x, -n)
