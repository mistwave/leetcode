class Solution(object):
        def compareVersion(self, version1, version2):
            """
            :type version1: str
            :type version2: str
            :rtype: int
            """
            v1 = version1.split('.')
            v2 = version2.split('.')
            l1 = len(v1)
            l2 = len(v2)
            maxLen = l1 if l1 > l2 else l2
            if l1 < maxLen:
                v1 += ['0'] * (l2 - l1)
            else:
                v2 += ['0'] * (l1 - l2)

            for a, b in zip(v1, v2):
                a, b = int(a), int(b)
                if a < b:
                    return -1
                elif a > b:
                    return 1
            return 0
