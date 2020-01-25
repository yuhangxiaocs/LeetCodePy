# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def construct(self, t):
        return 0


class Solution(object):

    # 利用二叉搜索树的性质 适当剪枝
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root == None:
            return 0

        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return root.val + self.rangeSumBST(root.right, L, R) + self.rangeSumBST(root.left, L, R)

    # 用stack来模拟递归 节约递归调用代价
    # python中用list的append和pop操作轻松实现stack
    def rangeSumBST2(self, root, L, R):
        stack = []
        stack.append(root)
        rangeSum = 0

        while (len(stack) > 0):
            node = stack.pop()
            if node == None:
                continue
            if node.val < L:
                stack.append(node.right)
            elif node.val > R:
                stack.append(node.left)
            else:
                rangeSum += node.val
                stack.append(node.left)
                stack.append(node.right)
        return rangeSum
