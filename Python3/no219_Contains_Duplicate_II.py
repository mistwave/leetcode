class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # to skip non-duplicate list
        if len(nums)==len(set(nums)) or k==0:
            return False
        d = {}
        for index, num in enumerate(nums):
            if num not in d:
                d[num] = index
            else:  # num in d
                if index - d[num] <= k:
                    return True
                else:  # update the index for later number
                    d[num] = index
        return False
