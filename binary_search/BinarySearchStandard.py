'''
    左开右闭的区间，hi永远是等于mid，

    注意它不会漏掉mid这个位置的值
'''


def lower_bound(nums, target):
    if not nums: return
    lo, hi = 0, len(nums)

    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1

    return lo


def upper_bound(nums, target):
    if not nums: return
    lo, hi = 0, len(nums)

    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] > target:
            hi = mid
        else:
            lo = mid + 1

    return lo


if __name__ == '__main__':
    nums = [4, 4, 4, 4, 4]
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 4

    print(lower_bound(nums, target))
    # print(upper_bound(nums, target))
