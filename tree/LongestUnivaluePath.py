# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    Given a binary tree, find the length of the longest path where each node in the path has the same value.
    This path may or may not pass through the root.

    The length of path between two nodes is represented by the number of edges between them.

    这道题依然使用递归来解，但是特殊性在于，难以将答案直接表示在返回值中，因为它的路径可能是跨越root的；
    helper辅助函数的返回值代表的是以当前root为根的最大长度，首先分别处理左右子树，如果发现左子树root的值等于
    当前root的值，那么当前的这个lp（lpath）就要+1，右边也是，然后下面比较的时候，是将他们两个加起来比较；
    但是返回的时候只能返回一个；

    也就是比较的时候使用左右合并结果，返回的时候只返回一个，用额外的变量来更新答案；
'''
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def helper(root):
            if not root: return 0

            l = helper(root.left) if root.left else -1
            r = helper(root.right) if root.right else -1


            lp = l + 1 if root.left and root.left.val == root.val else 0
            rp = r + 1 if root.right and root.right.val == root.val else 0



            self.res = max(self.res, lp + rp)

            return max(lp, rp)

        helper(root)

        return self.res
