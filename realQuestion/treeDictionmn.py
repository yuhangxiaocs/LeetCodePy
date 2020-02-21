import math
from collections import deque


def calKthNumber(n, k):
    # d --> 10^d - 1

    depth = 1

    while math.pow(10, depth) - 1 < n:
        depth += 1
    print(depth)
    treeSize = int(math.pow(10, depth - 1))
    # print(treeSize)
    x = k // treeSize
    indexOfTree = math.ceil(k / treeSize)
    indexOfNode = k % treeSize

    print(indexOfTree, indexOfNode)

    q = deque([str(indexOfTree)])
    res = [str(indexOfTree)]
    while q and indexOfNode > 0:
        n = q.popleft()
        print(n)
        res[0] = n
        indexOfNode -= 1
        for i in range(10):
            q.append(n + str(i))

    print(int(res[0]))


if __name__ == '__main__':
    calKthNumber(10000, 100)
