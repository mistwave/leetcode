class Solution(object):
    def longestPalindrome(self, s):
        length = len(s)
        start, maxlen = 0, 1
        for i in range(length):
            oddlen, evenlen, nowlen = 0, 0, 0
            oddlen = self.lenoflongestpalindrome(s, i, i)  # "abcba"

            if i + 1 < length:
                evenlen = self.lenoflongestpalindrome(s, i, i + 1)  # "abccba"

            nowlen = oddlen if oddlen > evenlen else evenlen

            if nowlen > maxlen:
                maxlen = nowlen
                if maxlen % 2:
                    start = i - (maxlen - 1) / 2
                else:
                    start = i - maxlen / 2 + 1

        return s[int(start):int(start) + maxlen]

    def lenoflongestpalindrome(self, s, left, right):
        length = len(s)
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - 1) - (left + 1) + 1

    def longestPalindrome_1(self, s):  # TLE
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        for nowlength in range(length, 0, -1):
            for j in range(length - nowlength + 1):  # the number of nowlength substring: length - nowlength + 1
                if self.isPalindrome(s[j:j + nowlength]):
                    return s[j:j + nowlength]
        return False

    def isPalindrome(self, s):
        for i in range(int(len(s) / 2)):
            if not s[i] == s[-1 - i]:
                return False
        return True


if __name__ == '__main__':
    testlist = ['a', 'bb', 'ccc', 'dddd', 'bbbbb', 'abcdsax', 'plbblp', 'tppttppt', 'jfdahdhsai']
    s = Solution()
    for str in testlist:
        print(str + ': ')
        print(s.longestPalindrome(str))
