# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def __init__(self):
        self.d = {}
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node is None:
            return None
        if node.label in self.d:
            return self.d[node.label]
        newnode = UndirectedGraphNode(node.label)
        self.d[node.label] = newnode
        for n in node.neighbors:
            newnode.neighbors.append(self.cloneGraph(n))
        return newnode
