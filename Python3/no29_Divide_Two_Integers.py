class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = ~MAX_INT
        if divisor == 0:
            return -1
        if dividend == 0:
            return 0
        isneg = True if (dividend > 0 and divisor < 0) or (
            dividend < 0 and divisor > 0) else False

        sumed, count, ans, a, b = 0, 0, 0, abs(dividend), abs(divisor)

        while a >= b:
            sumed = b
            count = 1
            while a >= sumed << 2:
                sumed = sumed << 2
                count = count << 2
            a -= sumed
            ans += count

        ans = ~ans + 1 if isneg else ans
        return ans if not (ans > MAX_INT or ans < MIN_INT) else MAX_INT
