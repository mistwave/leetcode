# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # recursively
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

        # iteratively
    def inorderTraversal_ite(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = []
        ans = []
        cur = root
        while cur or s:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                ans.append(cur.val)
                cur = cur.right
        return ans
