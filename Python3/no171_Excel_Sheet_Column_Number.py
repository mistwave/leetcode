class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        numoflet = lambda x: ord(x) - ord('A') + 1
        for i, c in enumerate(s[::-1]):
            ans += 26**i * numoflet(c)
        return ans
