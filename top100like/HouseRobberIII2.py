# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    '''
        通过前面的代码 看出很多重叠子问题 既然这样 保存起来 由于这里是树 所以保存在字典里而不是数组

        Runtime: 32 ms, faster than 94.07% of Python online submissions for House Robber III.
        Memory Usage: 16.8 MB, less than 14.29% of Python online submissions for House Robber III.
    '''

    def robber(self, root, dic):
        if not root: return 0

        if root in dic:
            return dic[root]

        val = 0

        if root.left:
            val += self.robber(root.left.left, dic) + self.robber(root.left.right, dic)

        if root.right:
            val += self.robber(root.right.left, dic) + self.robber(root.right.right, dic)

        dic[root] = max(root.val + val, self.robber(root.left, dic) + self.robber(root.right, dic))

        return dic[root]

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dic = {}
        return self.robber(root, dic)
