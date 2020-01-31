# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
