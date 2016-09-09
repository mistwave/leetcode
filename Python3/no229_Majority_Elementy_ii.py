class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            if num not in ans and nums.count(num) > len(nums) // 3:
                ans.append(num)
        return ans
