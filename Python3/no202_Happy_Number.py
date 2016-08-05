from functools import reduce


class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # special num : 0, 1
        s = []
        while n != 1:
            n = reduce(lambda x, y: x + y,
                       map(lambda x: int(x)**2, list(str(n))))
            if n == 0 or n in s:
                return False
            s.append(n)
        return True

if __name__ == '__main__':
    # test for special num
    for i in range(100000):
        if i == reduce(lambda x, y: x + y, map(lambda x: int(x)**2, list(str(i)))):
            print(i)
    print('end')
    # output: 0, 1
