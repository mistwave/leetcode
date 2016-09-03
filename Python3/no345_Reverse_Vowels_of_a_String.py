class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        s = list(s)
        vs = []
        vsi = []
        for i, c in enumerate(s):
            if c in vowels:
                vs.append(c)
                vsi.append(i)
        for i, c in zip(vsi[::-1], vs):
            s[i] = c
        return ''.join(s)
