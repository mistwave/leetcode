class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        commonprefix = ''
        for i in range(len(strs)):
            if i == 0:
                commonprefix = strs[i]
            else:
                commonprefix = self.getcommonprefix(commonprefix, strs[i])
        return commonprefix

    def getcommonprefix(self, str1, str2):
        i = 0
        length = min(len(str1), len(str2))
        while i < length and str1[i] == str2[i]:
            i += 1
        return str1[:i]

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['aa','abgjmiaoshiof','ajiofjs']))
    print(s.getcommonprefix('aa','ab'))