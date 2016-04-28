class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        leftside = ("(","[","{")
        rightside = (")","]","}")
        d = {")":"(","]":"[","}":"{"}
        for char in s:
            if char in leftside:
                stack.append(char)
            if char in rightside:
                if stack == []:
                    return False
                else:
                    if stack.pop() != d[char]:
                        return False
                    else:
                        pass


        return True if stack == [] else False
