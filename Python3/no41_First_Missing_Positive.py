class Solution(object):
    # bit manipulation solution
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1
        n = len(nums)
        # 1 stand for not seen
        # (n+1) not n: case input with [1,2,3]
        bitflag = 2**(n + 1) - 1
        # num: 0 b 1 0 1 1
        # index:   4 3 2 1
        # 1011->0,k=3
        getbit = lambda num, k: (num >> (k - 1)) & 1
        # 101101->101001,k=3
        setbitzero = lambda num, k: num & ~(1 << (k - 1))
        for num in nums:
            if num > 0 and getbit(bitflag, num) == 1:
                bitflag = setbitzero(bitflag, num)

        # 去掉右起第一个1的左边 | (10010 1000->1000) | x and (x xor (x-1))
        # ref: http://www.matrix67.com/blog/archives/263
        tmp = bitflag & (bitflag ^ (bitflag - 1))
        import math
        return int(math.log(tmp, 2) + 1)
