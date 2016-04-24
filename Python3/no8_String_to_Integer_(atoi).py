class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        space = ('\r', '\t', '\n', ' ')
        number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        pm = ('-', '+')
        status = ['error', 1, 2, 3, 4]  # define a FSM
        s = status
        cur = 1
        flag = 1
        rnum = 0
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        for char in str:
            if cur == s[1]:
                if char in space:
                    cur = s[1]
                elif char in pm:
                    cur = s[2]
                    if char == '-':    #negetive flag
                        flag = -1
                elif char in number:
                    cur = s[3]
                    rnum = rnum * 10 + int(char)
                else:
                    cur = s[0]
            elif cur == s[2]:
                if char in number:
                    cur = s[3]
                    rnum = rnum * 10 + int(char)
                else:
                    cur = s[0]
            elif cur == s[3]:
                if char in number:
                    cur = s[3]
                    rnum = rnum * 10 + int(char)
                # elif char in space:
                #     cur = s[4]
                else:
                    break
            # elif cur == s[4]:
            #     return flag * rnum
            else:  # error
                return 0

        rnum *= flag
        if rnum > MAX_INT:
            return MAX_INT
        elif rnum < MIN_INT:
            return MIN_INT
        else:
            return rnum


if __name__ == '__main__':
    testlist = ['123', '  123', '    321', '  +312', "  -123", "  +321 fansud", "  -44738ffda"]

    s = Solution()
    for str in testlist:
        print(str + ':')
        print(s.myAtoi(str))
