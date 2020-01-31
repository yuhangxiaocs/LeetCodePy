# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
注意是从root到leaf的路径
'''


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 到了空还没有出现和相等的情况 肯定是False
        if not root:
            return False
        # 这一步判断到leaf node的情况 只有这一种为真 其他都为假的
        if not root.left and not root.right and sum - root.val == 0:
            return True
        # python的 or 不是返回True or False 而是返回一个值
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)



# 为什么第一次想处理啊这个步骤 真是又臭又长 用sum去减 就可以了！
# def traverse(self, root, curSum, sum, res):
#     if not root:
#         return
#
#     if not root.left and not root.right and curSum + root.val == sum:
#         res.append('yes')
#         return
#
#     self.traverse(root.left, curSum + root.val, sum, res)
#     self.traverse(root.right, curSum + root.val, sum, res)
#
# def hasPathSum(self, root, sum):
#     """
#     :type root: TreeNode
#     :type sum: int
#     :rtype: bool
#     """
#     res = []
#
#     if not root:
#         return False
#
#     self.traverse(root, 0, sum, res)
