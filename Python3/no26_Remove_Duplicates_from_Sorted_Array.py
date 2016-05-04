class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newindex = 0
        curdigit = None
        for num in nums:
            if num != curdigit:
                nums[newindex] = num
                curdigit = num
                newindex += 1
        return newindex
