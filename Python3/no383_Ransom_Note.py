class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ran = [0] * 26
        mag = [0] * 26
        for c in magazine:
            if ord('a') <= ord(c) <= ord('z'):
                nc = ord(c) - ord('a')
                mag[nc] += 1
        for c in ransomNote:
            if ord('a') <= ord(c) <= ord('z'):
                nc = ord(c) - ord('a')
                ran[nc] += 1
                if ran[nc] > mag[nc]:
                    return False
        return True
