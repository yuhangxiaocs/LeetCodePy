"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res, stack = [], []

        p = root
        while p or stack:
            if p:
                res.append(p.val)
                stack.append(p)
                try:
                    tmp = p.children[0]
                    p.children.remove(tmp)
                    p = tmp
                except:
                    p = None
            else:
                node = stack.pop()
                try:
                    p = node.children[0]
                except:
                    p = None

        return res

    '''
        正是如此
    '''

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return
        res, stack = [], [root]
        list
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(reversed(node.children))


if __name__ == '__main__':
    obj = Solution()
