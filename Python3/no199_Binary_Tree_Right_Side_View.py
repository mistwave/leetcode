# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

        # inorder traversal solution
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        if root is None:
            return []
        queue = deque([root])
        ans = []
        while queue:
            length = len(queue)
            for i in range(length):
                cur = queue.popleft()
                if i == 0:
                    ans.append(cur.val)
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
        return ans

    def RSV_recursive(self, root):
        if root is None:
            return []
        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)
        return [root.val] + right + left[len(right):]

    def RSV_recursive_and_DFS(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def iter(node, depth):
            if node:
                if len(ans) == depth:
                    ans.append(node.val)
                iter(node.right, depth+1)
                iter(node.left, depth+1)
        ans = []
        iter(root, 0)
        return ans

