# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def invertTree_r(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # recursive
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTree_i(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # iterative way
        if root is None:
            return root
        from collections import deque
        q = deque()
        q.append(root)
        while len(q) > 0:
            now = q.popleft()
            if now.left:
                q.append(now.left)
            if now.right:
                q.append(now.right)
            now.left, now.right = now.right, now.left
        return root
