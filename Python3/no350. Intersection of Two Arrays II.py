class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 is None or nums2 is None:
            return None
        long, short = (nums1, nums2) if len(nums1) >= len(nums2) else (nums2, nums1)
        long.sort()
        res = []
        for i in short:
            if i in long:
                res.append(i)
                long.remove(i)
        return res
