class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
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
