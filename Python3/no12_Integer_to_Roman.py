class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digit = []
        roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
                 10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
                 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
                 1000: 'M', 2000: 'MM', 3000: 'MMM',
                 0: ''}
        while num:
            digit.append(num % 10)
            num = int(num / 10)
        for i in range(len(digit)):
            digit[i] = digit[i] * 10 ** i

        rstr = ''
        for x in digit:
            rstr = roman[x] + rstr
        return rstr

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
    for x in range(1,3999):
        assert x == s.romanToInt(s.intToRoman(x))
    print('test passed')
