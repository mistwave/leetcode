class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isalphanumeric(a):
            aa = ord(a)
            return True if (aa >= ord('a') and aa <= ord('z')) or (aa >= ord('0') and aa <= ord('9')) else False
        if s == "":
            return True
        ls = list(filter(isalphanumeric, s.lower()))
        return ls == ls[::-1]
