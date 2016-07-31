class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        p0, p2 = 0, N - 1
        i = 0
        while not (i > p2 or p0 > N - 1 or p2 < 0):
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                if i == p0:
                    i += 1
                    p0 += 1
                else:
                    if nums[i] != nums[p0]:  # do not change the equal value
                        nums[i], nums[p0] = nums[p0], nums[i]
                    p0 += 1
            elif nums[i] == 2:
                if nums[i] != nums[p2]:  # do not change the equal value
                    nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
