class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        length = len(nums)
        diff = MAX_INT
        if length < 3:
            return 0
        nums = sorted(nums)    # from small to big
        for first in range(length - 2):

            left, right = first + 1, length - 1
            while left < right:
                curdiff = nums[first] + nums[left] + nums[right] - target
                if abs(curdiff) < abs(diff):
                    diff = curdiff
                if curdiff == 0:
                    return diff + target
                elif curdiff < 0:
                    left += 1
                else:
                    right -= 1
        return diff + target


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([1,2,4,8,16,32,64,128],82))