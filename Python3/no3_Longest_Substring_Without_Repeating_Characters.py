class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen ,start = 0, 0
        isvisted = {}
        for i, char in enumerate(s):
            if char in isvisted:
                start = max(isvisted[char], start)
            maxlen = max(maxlen, i - start + 1)
            isvisted[char] = i + 1

        return maxlen

if __name__ == '__main__':
    s = Solution()
    assert 3 == s.lengthOfLongestSubstring('abcabcbbb')
    assert 10 == s.lengthOfLongestSubstring("fnshfqwopei")
    print("test passed")