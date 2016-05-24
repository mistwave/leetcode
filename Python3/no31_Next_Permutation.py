
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            pass # do nothing
        else: # len(nums) >= 2
            i = n - 2
            while i >= 0 and nums[i] >= nums[i+1]:
                i -= 1
            if i == -1:  # nums is in descending order: like 54321
                nums.sort()
            else:
                # nums[i+1:] is in descending: like 72543221
                # find last num which >= nums[i]
                j = i + 1
                while j < n and nums[j] > nums[i]:
                    j += 1
                # swap nums[i] and nums[j-1]
                tmp = nums[i]
                nums[i] = nums[j-1]
                nums[j-1] = tmp
                # !! in-place mutation
                nums[i+1:] = sorted(nums[i+1:])


def test():
    s = Solution()
    testlists = [[5,1,1],[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    result = [[1,1,5],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1],[1,2,3]]

    for i in range(len(testlists)):
        s.nextPermutation(testlists[i])
        assert testlists[i] == result[i]
    print("test pass")

if __name__ == '__main__':
    test()
