class Solution(object):
    # slow solution : 173ms
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for n in range(1, 10):
            if (self.hasrepeatednum(self.getline(board, n))
                    or self.hasrepeatednum(self.getrow(board, n))
                    or self.hasrepeatednum(self.getsubsudoku(board, n))):
                return False
        return True

    def getline(self, board, n):
        # line 1 to 9 from top to bottom
        return board[n - 1] if n <= 9 and n >= 1 else None

    def getrow(self, board, n):
        # row 1 to 9 from left to right
        if not (n <= 9 and n >= 1):
            return None
        ans = []
        for i in range(9):
            ans.append(board[i][n - 1])
        return ans

    def getsubsudoku(self, board, n):
        # subsudoku:
        #  1  2  3
        #  4  5  6
        #  7  8  9
        # :rtype: list
        if not (n <= 9 and n >= 1):
            return None
        ans = []
        d = dict()
        d.update({
                 1: [(i, j) for i in range(0, 3) for j in range(0, 3)],
                 2: [(i, j) for i in range(0, 3) for j in range(3, 6)],
                 3: [(i, j) for i in range(0, 3) for j in range(6, 9)],
                 4: [(i, j) for i in range(3, 6) for j in range(0, 3)],
                 5: [(i, j) for i in range(3, 6) for j in range(3, 6)],
                 6: [(i, j) for i in range(3, 6) for j in range(6, 9)],
                 7: [(i, j) for i in range(6, 9) for j in range(0, 3)],
                 8: [(i, j) for i in range(6, 9) for j in range(3, 6)],
                 9: [(i, j) for i in range(6, 9) for j in range(6, 9)]
                 })
        for i, j in d[n]:
            ans.append(board[i][j])
        return ans

    def hasrepeatednum(self, list):
        shown = set()
        for i in list:
            if i != '.' and i in shown:
                return True
            else:
                shown.add(i)
        return False
