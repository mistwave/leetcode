class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        sample, result = [], []
        self.validposition(n, 0, sample, result)
        return [] if result == [] else self.printresult(result)
        # return result

    def validposition(self, n, nalready, sample, result):
        if nalready == n:
            result.append(sample[:])  # shallow copy
            return
        else:
            for i in range(n):
                sample.append(i)
                if self.isnewestvalid(sample):
                    self.validposition(n, nalready + 1, sample, result)
                sample.pop()

    def isnewestvalid(self, sample):
        newpos = sample[-1]
        newindex = len(sample) - 1
        for index, pos in enumerate(sample[:-1]):
            if pos == newpos or (index + pos) == (newpos + newindex) or (index - pos) == (newindex - newpos):
                return False
        return True

    def printresult(self, result):
        allprint = []
        n = len(result[0])

        for re in result:
            curprint = []
            for line in re:
                curprint.append("Q".join(["." * line, "." * (n - line - 1)]))
            allprint.append(curprint)
        return allprint


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 6):
        print(s.solveNQueens(i))
