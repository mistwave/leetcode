# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = []
        ans = []
        while root or s:
            if root:
                ans.append(root.val)
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                root = root.right
        return ans
