from collections import deque


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
        if not root: return

        q = deque()
        q.append(root)
        pre = 0
        while q:
            res = 0
            x = len(q)
            # 这里只要取出一层的所有，并将它们的孩子都添加到队列中做后序处理
            while x:
                node = q.popleft()
                res += node.val
                x -= 1
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            pre = res
        return pre

    '''
        Lee215 code, so so so niubility!
        它这里p q是把每层node放到一个list中 最后再求和
    '''

    def deepestLeavesSum(self, root):
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(100)

    print(Solution().deepestLeavesSum(root))
