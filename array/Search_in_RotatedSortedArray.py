'''
    https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1

        def findLeast(nums, lo, hi):
            while lo + 1 < hi:
                mid = (lo + hi) // 2

                if nums[mid] <= nums[hi]:
                    hi = mid

                elif nums[mid] >= nums[lo]:
                    lo = mid

            return hi

        p = findLeast(nums, 0, len(nums) - 1)

        def bisearch(nums, lo, hi, target):

            while lo <= hi:
                mid = lo + (hi - lo) // 2

                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            return -1

        x = bisearch(nums, 0, p - 1, target)
        y = bisearch(nums, p, len(nums) - 1, target)

        if x == -1 and y == -1: return -1

        if x >= 0: return x
        if y >= 0: return y


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 8, 1, 2, 3]
    # nums = [1, 2, 3, 4, 5]
    # nums = [1, 2, 1, 1, 1]

    print(findLeast(nums, 0, len(nums) - 1))
