class Solution(object):

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s, t = list(pattern), str.split()
        if len(s) != len(t):
            return False
        sMap, tMap = {}, {}
        for i in range(len(s)):
            src, tar = sMap.get(t[i]), tMap.get(s[i])
            if src is None and tar is None:
                sMap[t[i]] = s[i]
                tMap[s[i]] = t[i]
            elif tar != t[i] or src != s[i]:
                return False
        return True

    # https://leetcode.com/discuss/62333/short-in-python
    def wordPattern_short(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s, t = list(pattern), str.split()
        return map(s.index, s) == map(t.index, t)
