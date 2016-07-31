class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        # ans = [0, 10]
        # for i in range(2, 11):
        #     ans.append(int(ans[-1] + 9 * fac[9]/fac[10-i]))
        # ans[0] = 1
        return [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851, 5611771, 8877691][n]
