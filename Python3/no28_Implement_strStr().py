class Solution(object):
    # brute solution

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(haystack)
        l2 = len(needle)
        if l2 == 0 or haystack == needle:
            return 0
        if l2 > l1:
            return -1

        for i in range(l1 - l2 + 1):
            if haystack[i:i + l2] == needle:
                return i
        return -1
