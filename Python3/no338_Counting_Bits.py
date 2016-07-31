class Solution(object):

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0, 1]
        this = [1]
        while len(ans) < num + 1:
            that = this[:]
            for i in range(len(this)):
                that[i] += 1
            this += that
            ans += this
        return ans[:num + 1]
