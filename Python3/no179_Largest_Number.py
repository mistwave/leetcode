class Solution:
    # @param {integer[]} nums
    # @return {string}

    def largestNumber(self, nums):
        from functools import cmp_to_key
        sorted_nums = sorted([str(x) for x in nums], key=cmp_to_key(
            lambda a, b: int(a + b) - int(b + a)))[::-1]
        return '0' if nums == [] or set(nums) == {0} else ''.join(sorted_nums)

    def largestNumber1(self, nums):

        def lessorequal(a, b):
            # return True if a <= b, say, ab <= ba
            from math import log10
            if a == 0:
                return True
            elif b == 0 and a != 0:
                return False
            elif int(log10(a)) == int(log10(b)):  # 3 and 8; 22 and 13
                return a <= b
            else:
                return a * 10**int(log10(b) + 1) + b <= b * 10**int(log10(a) + 1) + a

        def quick_sort(nums):
            _quick_sort(nums, 0, len(nums) - 1)
            return nums

        def _quick_sort(nums, p, r):
            if p >= r:
                return
            q = _partition(nums, p, r)
            _quick_sort(nums, p, q - 1)
            _quick_sort(nums, q + 1, r)
        # partition for quick sort

        def _partition(nums, p, r):
            x = nums[r]
            i = p - 1
            for j in range(p, r):
                if lessorequal(nums[j], x):
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        # insertion sort for short list
        # def my_insertion_sort(nums):
        #     for i in range(1, len(nums)):
        #         j = i - 1
        #         while j >= 0 and less(nums[j + 1], nums[j]):
        #             nums[j + 1], nums[j] = nums[j], nums[j + 1]
        #             j -= 1
        #     return nums
        if nums == [] or set(nums) == {0}:
            return "0"
        ans = ''
        for item in quick_sort(nums)[::-1]:
            ans += str(item)
        return ans
