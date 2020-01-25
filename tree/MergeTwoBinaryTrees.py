# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val += t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1

    def mergeTrees(self, t1, t2):

        stack1 = []
        stack2 = []
        stack1.append(t1)
        stack2.append(t2)

        while len(stack2) > 0 and len(stack1) > 0:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if node1 == None or node2 == None:
                continue

            node1.val += node2.val


        return 
