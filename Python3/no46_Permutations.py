class Solution(object):

    def permute(self, nums):
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
            for i in range(len(nums)):
                newnums = nums[:]
                newnums.pop(i)
                cur.append(nums[i])
                self.helper(newnums, cur, result)
                cur.pop()

if __name__ == '__main__':
    s = Solution()
    assert [] == s.permute([])
    assert sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [
                  3, 1, 2], [3, 2, 1]]) == sorted(s.permute([1, 2, 3]))
    print("test pass")
