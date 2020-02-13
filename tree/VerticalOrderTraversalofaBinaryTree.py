from collections import OrderedDict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import OrderedDict


class Solution(object):
    '''
        存在上下错乱
    '''
    # def verticalTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     if not root: return
    #
    #     dic = OrderedDict()
    #
    #     def preOrder(root, pos):
    #         if not root: return pos
    #
    #         if pos not in dic:
    #             dic[pos] = [root.val]
    #         else:
    #             dic[pos].append(root.val)
    #
    #         preOrder(root.left, pos - 1)
    #
    #         preOrder(root.right, pos + 1)
    #
    #     preOrder(root, 0)
    #     print(dic)

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return

        vals = []

        def preOrder(root, x, y):
            if not root: return
            vals.append((x, y, root.val))
            preOrder(root.left, x - 1, y + 1)
            preOrder(root.right, x + 1, y + 1)

        preOrder(root, 0, 0)
        res = []
        lastx = -99999
        for x, y, val in sorted(vals):
            if x != lastx:
                res.append([])
                lastx = x
            res[-1].append(val)

        return res
        return list(dic.values())


if __name__ == '__main__':
    print()
