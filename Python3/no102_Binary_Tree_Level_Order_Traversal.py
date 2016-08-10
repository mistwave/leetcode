# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        from collections import deque

        q = deque()
        level = 0
        q.append((level, root))
        ans = []
        while q:
            cur = q.popleft()
            level = cur[0]
            if cur[1].left: q.append((level+1, cur[1].left))
            if cur[1].right: q.append((level+1, cur[1].right))
            ans.append([cur[0], cur[1].val])
        ret = [[] for i in range(ans[-1][0]+1)]
        for x in ans:
            ret[x[0]].append(x[1])
        return ret


