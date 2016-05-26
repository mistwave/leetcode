class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.n = len(nums)
        return [self.searchLeftBoundary(nums, target), self.searchRightBoundary(nums, target)]

    def searchLeftBoundary(self, nums, target):
        start, end = 0, self.n - 1
        while start <= end:
            mid = int(start + (end - start) / 2)
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:  # target == nums[mid]
                end = mid - 1
        return start if nums[start] == target and start >= 0 and start < self.n else -1

    def searchRightBoundary(self, nums, target):
        start, end = 0, self.n - 1
        while start <= end:
            mid = int(start + (end - start) / 2)
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:  # target == nums[mid]
                start = mid + 1
        return end if nums[end] == target and end >= 0 and end < self.n else -1
