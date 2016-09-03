class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == "":
            return t
        ans = 0
        for char in s + t:
            ans = ans ^ ord(char)
        return chr(ans)
