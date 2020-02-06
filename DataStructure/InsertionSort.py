'''
    插入排序 打牌是一样的 每接一张新牌 都从后向前看应该插入到哪里
    插入排序最好情况：数组有序，变成线性时间
           最坏情况：数组逆序，退化成N^2时间
    从第二个元素开始插入，对于第i个元素，首先将a[i]的值记录下来防止覆盖
    然后循环找到插入位置
'''


def insertinoSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j > 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums


if __name__ == '__main__':
    nums = [1, 2, 4, 8, 6, 1, 8, 9, 7, 5]
    print(nums)

    print(insertinoSort(nums))
