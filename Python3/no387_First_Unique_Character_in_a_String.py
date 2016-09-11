class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        d1 = set()
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for key in d:
            if d[key] == 1:
                d1.add(key)
        for i, c in enumerate(s):
            if c in d1:
                return i
        return -1
