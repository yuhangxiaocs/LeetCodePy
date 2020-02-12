# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def deep(root, depth):
            if not root:
                return [depth, None]

            [ld, lv] = deep(root.left, depth + 1)
            [rd, rv] = deep(root.right, depth + 1)

            if lv == None and rv == None:
                return [depth, root.val]

            if lv == None and rv != None:
                return [rd, rv]
            if lv != None and rv == None:
                return [ld, lv]

            if ld == rd:
                return [ld, lv + rv]
            else:
                return max([ld, lv], [rd, rv])

        a, b = deep(root, 0)

        return b


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(100)

    print(Solution().deepestLeavesSum(root))
