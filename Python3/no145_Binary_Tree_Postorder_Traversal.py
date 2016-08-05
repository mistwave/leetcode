# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = Nonea


class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        s = []
        pre = None
        while root or s:
            if root:
                s.append(root)
                root = root.left
            elif s[-1].right != pre:  # deal with left subtree
                root = s[-1].right
                pre = None
            else:  # left and right subtree covered
                pre = s.pop()
                ans.append(pre.val)
        return ans
