class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        newindex = 0
        for i in range(length):
            if nums[i] != val:
                nums[newindex] = nums[i]
                newindex += 1
        return newindex

    # v1 wrong answer
    # Your input

    # [3,2,2,3]
    # 3
    # [2,3,4,5,6,7,8,7,6,5,4,4,5,6,7,6,6,5,5,4,4]
    # 4
    # Your answer

    # [3,2]
    # [2,3,4,5,6,7,8,7,6,5,4,4,5,6,7,6]
    # Expected answer

    # [2,2]
    # [2,3,5,6,7,8,7,6,5,5,6,7,6,6,5,5]
    def removeElement_v1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        rnum = length
        for i in range(length):
            if nums[i] == val:
                rnum -= 1
        return rnum

