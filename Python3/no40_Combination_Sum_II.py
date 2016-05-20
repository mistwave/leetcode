class Solution(object):

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if candidates == [] or candidates is None:
            return []
        result = []
        self.iter(candidates, target, 0, [], result)
        return result

    def iter(self, candidates, target, num, chosen, result):
        if target == 0:
            tmp = chosen[:]
            tmp.sort()
            if tmp not in result:
                result.append(tmp[:])
        elif target < 0:
            pass
        else:  # target > 0
            for i in range(num, len(candidates)):
                chosen.append(candidates[i])
                self.iter(candidates, target -
                          candidates[i], i + 1, chosen, result)
                del chosen[-1]
