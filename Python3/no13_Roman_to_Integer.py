class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # metanum = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        #            'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        #            'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        #            'M': 1000}
        metanum = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        strlist = []
        numlist = []
        for c in s:
            strlist.append(c)
            numlist.append(metanum[c])

        allsum = sum(numlist)
        allminus = 0
        for i in range(len(numlist) - 1):
            if numlist[i] < numlist[i + 1]:
                allminus += numlist[i]

        return allsum - 2 * allminus


if __name__ == '__main__':
    s = Solution()
    # print(s.romanToInt('MCDXXXVII'))
    # print(s.romanToInt('VII'))
    # print(s.romanToInt('XCIX'))
    # print(s.romanToInt('MDCCCLXXX'))
    # print(s.romanToInt('MMMCCCXXXIII'))

    assert s.romanToInt('MCDXXXVII') == 1437
    assert s.romanToInt('VII') == 7
    assert s.romanToInt('XCIX') == 99
    assert s.romanToInt('MDCCCLXXX') == 1880
    assert s.romanToInt('MMMCCCXXXIII') == 3333

    print("test finished")
