class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        helper = lambda nums: [nums[-1]] + nums[0:-1]

        N = len(matrix[0])
        if N in (0, 1):
            pass

        elif N % 2 == 1: # N is odd
            n = int((N-1)/2)
            # handle the axis
            for i in range(n):
                tochange = [matrix[i][n], matrix[n][N-1-i], matrix[N-1-i][n], matrix[n][i]]
                matrix[i][n], matrix[n][N-1-i], matrix[N-1-i][n], matrix[n][i] = helper(tochange)
            # handle the rest
            for i in range(n):
                for j in range(n):
                    tochange = [matrix[i][j], matrix[j][N-1-i], matrix[N-1-i][N-1-j], matrix[N-1-j][i]]
                    matrix[i][j], matrix[j][N-1-i], matrix[N-1-i][N-1-j], matrix[N-1-j][i] = helper(tochange)
        else: # N is even
            n = int(N/2)
            for i in range(n):
                for j in range(n):
                    tochange = [matrix[i][j], matrix[j][N-1-i], matrix[N-1-i][N-1-j], matrix[N-1-j][i]]
                    matrix[i][j], matrix[j][N-1-i], matrix[N-1-i][N-1-j], matrix[N-1-j][i] = helper(tochange)




if __name__ == '__main__':
    tests = [[[1]],
             [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]],
             [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],
             [[1,2,3],[4,5,6],[7,8,9]]]
    s = Solution()
    for x in tests:
        origin = x[:]
        s.rotate(x)
        assert origin == x
    print("test pass")
