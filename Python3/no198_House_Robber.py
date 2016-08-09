class Solution(object):

    # assume ans[i] stands for i-houses maximum amount of money
    # then ans[i] = max(ans[i-1], ans[i-2] + num[i])

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(nums[0])
            elif i == 1:
                ans.append(max(nums[0:2]))
            else:
                ans.append(max(ans[-1], ans[-2] + nums[i]))

        return ans[-1] if ans else 0

