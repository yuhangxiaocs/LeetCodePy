# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    Given a binary tree, you need to compute the length of the diameter of the tree.
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    This path may or may not pass through the root.


    @time: 2020-02-18
    这里就是比较特殊的情况，结果由左右子树拼凑而来，但是返回的时候只返回一个子树。

'''
class Solution(object):
    def __init__(self):
        self.maxx = -100

    def height(self, root):
        if not root:
            return 0

        le = self.height(root.left)
        ri = self.height(root.right)
        self.maxx = max(self.maxx, le + ri)
        return max(le, ri) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # edge case
        if not root:
            return 0
        # 最大值一定是左边和右边加起来的情形
        # 如果最大值出现在左子树中 那么在加上左子树的根节点 和右边的阶段 又会更大 所以一定是跨越左右子树的
        self.height(root)

        return self.maxx
