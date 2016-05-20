class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if candidates == [] or candidates is None:
            return []
        candidates.sort()
        result = []
        self.iter(candidates, target, 0, [], result)

        return result

    def iter(self, candidates, target, num, chosen, result):
        if target == 0:
            result.append(chosen[:])
            return None
        elif target < 0:
            return None
        else:  # target > 0
            for i in range(num, len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                chosen.append(candidates[i])
                self.iter(candidates, target -
                          candidates[i], i, chosen, result)
                del chosen[-1]
