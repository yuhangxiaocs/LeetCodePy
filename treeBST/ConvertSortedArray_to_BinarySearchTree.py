# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    我的思路是这样的，既然要平衡，每次取中间的元素插入，这样左右一定是相等的，如此递归下去即可，但是此方法很慢

    靠 知道了 这里的插入 为什么要这么麻烦啊 都已经是有序的了，所以每次直接取中点赋值给root 然后左边和右边子数组的中点
    分别取出来赋给左右子树即可
'''


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return

        def insertIntoBST(root, val):
            if not root: return TreeNode(val)
            if val <= root.val:
                root.left = insertIntoBST(root.left, val)
            else:
                root.right = insertIntoBST(root.right, val)

            return root

        self.root = None

        def insert(root, lo, hi):
            if lo <= hi:
                mid = (lo + hi) // 2
                self.root = insertIntoBST(self.root, nums[mid])
                insert(self.root, lo, mid - 1)
                insert(self.root, mid + 1, hi)

        insert(self.root, 0, len(nums) - 1)

        return self.root
