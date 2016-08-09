# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """


        s = []
        cnt = 0
        cur = root
        while cur or s:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                cnt += 1
                if cnt == k:
                    return cur.val
                cur = cur.right


