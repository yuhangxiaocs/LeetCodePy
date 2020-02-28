'''
    高娜德洗牌算法：

    Knuth 洗牌算法


    一个好的洗牌算法最重要的属性是公平，换句话说一副牌54张，共有54！种排列，好的算法要能保证任意一种排列都是等概率的。

    转换问题：对于每张牌，它在每个位置都是等可能出现的。

    算法思想如下：对于一个数组，从后往前，对于i元素，在[0, i]区间随机选个数与i位置的交换即可。

    比如原始 1 2 3 4 5这个数组，从5处开始，此时随机选取一个元素和当前交换，任何数字被交换到这里的概率都是1/5，
    接着对于下个位置，对于余下的所有数，交换到这里的概率是 4/5 * 1/4 = 1/5 ，以此类推，可得所有的位置都是等概率的。
'''

import random


def shuffle(arr):
    for i in range(len(arr) - 1, -1, -1):
        # [0, i]
        index = random.randrange(i + 1)

        arr[i], arr[index] = arr[index], arr[i]

    return arr


if __name__ == '__main__':

    origin = [1, 2, 3, 4]
    shuffled = shuffle(origin)
    print(shuffled)

    for i in range(100):
        print(random.randrange(10))
