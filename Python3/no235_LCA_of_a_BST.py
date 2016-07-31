# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def lowestCommonAncestor_recursively(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # to search for p or q
        # 204ms
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right
        # if left is None and right:
        #     return right
        # elif right is None and left:
        #     return left
        # elif right and left: # one node is in left and another is in right
        #     return root
        # else:
        #     return None

        # brilliant solution for BST
        # 140ms
    def lowestCommonAncestor_BSTway(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ans = root
        while ans:
            if min(p.val, q.val) > ans.val and ans.right:
                ans = ans.right
                continue
            elif max(p.val, q.val) < ans.val and ans.left:
                ans = ans.left
                continue
            return ans

        # 116ms
    def lowestCommonAncestor_pathway(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def path(root, p):
            s = []
            now = root
            while now and now.val != p.val:
                s.append(now)
                now = now.left if now.val > p.val else now.right
            s.append(now)
            return s

        pathP, pathQ = path(root, p), path(root, q)
        ans, i = None, 0
        minlen = min(len(pathP), len(pathQ))
        while i < minlen and pathP[i] == pathQ[i]:
            ans = pathP[i]
            i += 1
        return ans
