class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createBST(nums):
    root = None
    for num in nums:
        root = insert(root, num)

    return root


def insert(root, x):
    if not root:
        return TreeNode(x)

    if x <= root.val:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)

    return root


def inorderR(root):
    if not root:
        return
    inorderR(root.left)
    print(root.val, end=' ')
    inorderR(root.right)


def inorderTraversal(root):
    res, stack = [], []
    p = root
    while stack or p:
        if p:
            stack.append(p)
            p = p.left
        else:
            node = stack.pop()
            res.append(node.val)
            p = node.right

    return res


def preorderR(root):
    if not root: return

    print(root.val, end=" ")
    preorderR(root.left)
    preorderR(root.right)


def preorder(root):
    stack = []
    p = root
    while p or stack:
        if p:
            print(p.val, end=" ")
            stack.append(p)
            p = p.left

        else:
            node = stack.pop()
            p = node.right


if __name__ == '__main__':
    root = createBST([5, 3, 1, 4, 7, 6])
    preorderR(root)
    print()
    preorder(root)
    # inorder(root)

