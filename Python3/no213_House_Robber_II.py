class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def iter(nums):
            ans = []
            for i in range(len(nums)):
                if i == 0:
                    ans.append(nums[0])
                elif i == 1:
                    ans.append(max(nums[0:2]))
                else:
                    ans.append(max(ans[-1], ans[-2] + nums[i]))

            return ans[-1] if ans else 0
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(iter(nums[1:]), iter(nums[0:-1]))
