# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def traverse(self,root, psum, sum, res):
        if psum == sum:
            res += 1
        if root == None:
            return

        if psum == 0:
            self.traverse(root.left, psum, sum, res)
            self.traverse(root.left, psum + root.val, sum, res)
            self.traverse(root.right, psum, sum, res)
            self.traverse(root.right, psum + root.val, sum, res)
        else:
            self.traverse(root.left, psum + root.val, sum, res)

            self.traverse(root.right, psum + root.val, sum, res)




    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        res = 0
        self.traverse(root, 0, sum, res)
        return res
