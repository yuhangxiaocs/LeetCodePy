# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preOrder(root):
            if not root: return

            res.append(str(root.val))
            res.append(',')
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)

        res.pop()
        res.append(';')

        def inOrder(root):
            if not root: return
            inOrder(root.left)
            res.append(str(root.val))
            res.append(',')
            inOrder(root.right)

        inOrder(root)
        res.pop()

        return ''.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(';')
        preOrder = list(map(int, data[0].split(',')))
        inOrder = list(map(int, data[1].split(',')))

        print(preOrder)
        print(inOrder)

        def reBuild(pre, inOrder):

            if not pre: return

            # root value
            val = pre[0]
            pos = 0
            while pos < len(inOrder) and inOrder[pos] != val:
                pos += 1

            root = TreeNode(val)

            if not pre:
                pre.pop(0)
                root.left = reBuild(pre, inOrder[:pos])

            if not pre:
                pre.pop(0)
                root.right = reBuild(pre, inOrder[pos + 1:])

            return root

        return reBuild(preOrder, inOrder)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)
    obj = Codec()
    s = obj.serialize(root)

    res = obj.deserialize(s)

    print(res.val)
    print(res.left.val)
    print(res.right.val)
