# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # O(nlogn)
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        elif head.next is None:
            return TreeNode(head.val)
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        root = TreeNode(slow.next.val)
        root.right = self.sortedListToBST(slow.next.next)
        # !!! CUT DOWN THE LIST
        slow.next = None
        root.left = self.sortedListToBST(head)
        return root

