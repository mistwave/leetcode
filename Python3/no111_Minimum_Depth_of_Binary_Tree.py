# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left and root.right is None:
            return self.minDepth(root.left) + 1
        elif root.left is None and root.right:
            return self.minDepth(root.right) + 1
        else: # root.left and root.right
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

