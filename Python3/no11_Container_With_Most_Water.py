class Solution(object):
    # O(N^2) solution TLE
    # def maxArea(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     maxcap = 0
    #     length = len(height)
    #     for left in range(length - 1):
    #         for right in range(left + 1, length):
    #             tmpcap = height[left] * (right - left) if height[left] <= height[right] else height[right] * (right - left)
    #             if maxcap < tmpcap:
    #                 maxcap = tmpcap
    #     return maxcap

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxcap = 0
        left, right = 0, len(height)-1
        while left < right:
            curcap = min(height[left], height[right]) * (right - left)
            if curcap > maxcap:
                maxcap = curcap

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxcap

if __name__ == '__main__':
    testcase = [[1,2,4,5,6,2,2,3]]
    s = Solution()
    for t in testcase:
        print('{0}: {1}'.format(t, s.maxArea(t)))