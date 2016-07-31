class Solution(object):

    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        this = maxsum = 0
        for i in range(len(nums)):
            this += nums[i]
            if this > maxsum:
                maxsum = this
            elif this < 0:
                this = 0
        return maxsum if maxsum != 0 else max(nums)

    def maxSubArray(self, nums):
        """
        http://alfred-sun.github.io/blog/2015/03/11/ten-basic-algorithms-for-programmers/
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        start = maxsum = nums[-1]
        for i in range(N - 2, -1, -1):
            start = max(nums[i], start + nums[i])
            maxsum = max(start, maxsum)
        return maxsum
