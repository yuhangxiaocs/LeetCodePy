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


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)


if __name__ == '__main__':
    root = createBST([5, 3, 1, 4, 7, 6])

    inorder(root)
