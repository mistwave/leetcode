class Solution(object):

    # O(Nlog(N))
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return len(citations)


    def hIndex2(self, citations):
        N = len(citations)
        log = [0] * (N + 1)
        for i in range(N):
            if citations[i] >= N:
                log[N] += 1
            else:
                log[citations[i]] += 1
        cnt = 0
        for i in range(N + 1)[::-1]:
            cnt += log[i]
            if cnt >= i:
                return i


