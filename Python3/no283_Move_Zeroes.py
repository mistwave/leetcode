class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z = 0
        for nz in range(len(nums)):
            if nums[nz]:
                nums[nz], nums[z] = nums[z], nums[nz]
                z += 1