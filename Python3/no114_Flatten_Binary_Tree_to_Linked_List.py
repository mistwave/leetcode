# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # preorder traversal
        s = []
        nodes = []
        while root or s:
            if root:
                nodes.append(root)
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                root = root.right
        # link the node in nodes
        if len(nodes) > 1:
            for i in range(len(nodes) - 1):
                nodes[i].left, nodes[i].right = None, nodes[i+1]
            nodes[-1].left = nodes[-1].right = None

    def flatten_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def iter(root):
            if root is None or (root.left is None and root.right is None):
                return root
            lefttail = iter(root.left)
            righttail = iter(root.right)
            if lefttail:
                lefttail.right = root.right
                root.right = root.left
                root.left = None

            # 3 conditions:
            # right subtree is not None;
            # left subtree is not None and right subtree is None;
            # just root
            if righttail:
                return righttail
            if lefttail:
                return lefttail
            return root

        root = iter(root)

    def flatten_morris_traversal(self, root):
        # eliminate each level's root's left child
        while root:
            if root.left:
                p = root.left
                while p.right: p = p.right
                p.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
