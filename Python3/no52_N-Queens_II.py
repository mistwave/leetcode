class Solution(object):

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        sample = []
        self.result = 0
        self.validposition(n, 0, sample)
        return self.result

    def validposition(self, n, nalready, sample):
        if nalready == n:
            self.result += 1  # shallow copy
            return
        else:
            for i in range(n):
                sample.append(i)
                if self.isnewestvalid(sample):
                    self.validposition(n, nalready + 1, sample)
                sample.pop()

    def isnewestvalid(self, sample):
        newpos = sample[-1]
        newindex = len(sample) - 1
        for index, pos in enumerate(sample[:-1]):
            if pos == newpos or (index + pos) == (newpos + newindex) or (index - pos) == (newindex - newpos):
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    for i in range(1, 10):
        print(s.totalNQueens(i))
