class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        sample = ""
        self.findParenthesis(n,0,0,sample,result)
        return result

    def findParenthesis(self, n, nleft, nright, sample, result):
        if n == nleft and n == nright:
            result.append(sample)
            return

        if nleft < n:
            sample += '('
            self.findParenthesis(n, nleft + 1, nright, sample, result)
            sample = sample[:-1]

        if nright < nleft:
            sample += ')'
            self.findParenthesis(n, nleft, nright + 1, sample, result)
            sample = sample[:-1]
