from collections import deque

'''
    Runtime: 12 ms, faster than 99.38% of Python online submissions for Binary Tree Level Order Traversal.
    Memory Usage: 12.4 MB, less than 27.94% of Python online submissions for Binary Tree Level Order Traversal.
'''


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return

        res = []
        q = deque()
        q.append([1, root])

        while q:
            level, node = q.popleft()
            if level <= len(res):
                res[level - 1].append(node.val)
            else:
                res.append([node.val])

            if node.left: q.append([level + 1, node.left])
            if node.right: q.append([level + 1, node.right])

        return res


if __name__ == '__main__':
    res = []
    print(len(res))
