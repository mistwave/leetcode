class Solution(object):
    # 2-num hash solution 228ms
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 4:
            return []
        L = set()
        sumsIndexes = {}
        for i in range(n):
            for j in range(i + 1, n):
                cursum = nums[i] + nums[j]
                if cursum in sumsIndexes:
                    sumsIndexes[cursum].append((i,j))
                else:
                    sumsIndexes[cursum] = [(i,j)]

        for i in range(n):
            for j in range(i + 1, n):
                rest = target - (nums[i] + nums[j])
                if rest in sumsIndexes:
                    for index in sumsIndexes[rest]:
                        if index[0] > j:
                            L.add(tuple(sorted([nums[i],nums[j],nums[index[0]],nums[index[1]]])))

        rlist = []
        for l in L:
            rlist.append(list(l))
        return rlist

    #1764ms
    def fourSum_slow(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        L = []
        n = len(nums)
        for first in range(n - 3):
            for second in range(first+1, n - 2):
                d = dict()
                for index, value in enumerate(nums[second+1:], second + 1):
                    rest = target - value - nums[first] - nums[second]
                    if rest in d:
                        L.append(sorted([nums[first], nums[second], nums[index], rest]))
                    d[value] = index
        rlist = []
        for list in L:
            if list not in rlist:
                rlist.append(list)
        return sorted(rlist)

if __name__ == "__main__":
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
