'''
    peak is defined as

'''
import random


def peek_finder_1d(arr):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if mid - 1 >= 0 and arr[mid] < arr[mid - 1]:
            hi = mid - 1
        elif mid + 1 < len(arr) and arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            return mid


if __name__ == '__main__':
    arr = [random.randint(0, 100) for _ in range(100000)]
    # arr = [3, 2, 1]
    # arr = [1, 2, 3]
    # print(arr)
    x = peek_finder_1d(arr)
    print(arr[x - 1], arr[x], arr[x + 1])
    # print(peek_finder_1d(arr))
