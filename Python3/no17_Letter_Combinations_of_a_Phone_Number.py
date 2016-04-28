class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        di = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz",'0':" "}
        def iter(digits, rlist):
            if digits == "":
                return rlist
            else:
                tmp = []
                if rlist == []:
                    import itertools as it
                    tmp = list(it.islice(di[digits[0]], None))
                else:
                    for a in rlist:
                        for d in di[digits[0]]:
                            tmp.append(a + d)
                return iter(digits[1:],tmp)

        return iter(digits, [])

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("22"))