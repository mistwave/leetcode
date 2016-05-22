class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        result = []
        self.helper(nums, [], result)
        return result

    def helper(self, nums, cur, result):
        if nums == []:
            result.append(cur[:])
        else:
            seen = set()
            for i in range(len(nums)):
                if nums[i] not in seen:  # skip duplicated value
                    seen.add(nums[i])
                    newnums = nums[:]
                    newnums.pop(i)
                    cur.append(nums[i])
                    self.helper(newnums, cur, result)
                    cur.pop()
