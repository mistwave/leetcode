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

        start = maxsum = nums[0]
        for num in nums[1:]:
            start = max(num, start + num)
            maxsum = max(maxsum, start)
        return maxsum
