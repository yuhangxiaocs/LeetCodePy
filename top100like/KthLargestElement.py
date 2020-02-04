class Solution(object):
    # 找出第k大的数，思路是这样的，利用快速排序的划分将数组分为三段
    # [lo... pos-1] [pos] [pos+1...hi]
    # 如果 pos到hi正好等于k 就返回nums[pos] 刚好
    # 如果 右边的元素多于k 就在右边继续寻找 第 k 大
    # 如果右边元素小于 k 就在左边找  第 k-righttotal大的数

    def patition(self, nums, lo, hi):

        # print(nums[:])
        pivot = nums[lo]
        i, j = lo, hi

        while True:
            # 1 2 3 4 5
            while i < j and nums[j] > pivot:
                j -= 1
            while i < j and nums[i] <= pivot:
                i += 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break

        nums[lo], nums[i] = nums[i], nums[lo]
        # print(i)
        # print(nums[lo:hi + 1])
        return i

    def find(self, nums, lo, hi, k):

        pos = self.patition(nums, lo, hi)

        if hi - pos + 1 == k:
            return nums[pos]
        elif hi - pos + 1 > k:
            return self.find(nums, pos + 1, hi, k)
        else:
            return self.find(nums, lo, pos - 1, k - hi + pos - 1)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.find(nums, 0, len(nums) - 1, k)


if __name__ == '__main__':
    s = Solution()

    a = [5, 2, 4, 8, 6, 1, 8, 9, 7, 5]
    # a = [1, 2, 3, 4, 5]
    # a = [1, 1, 1, 1, 1]
    # print(s.findKthLargest())
    print(s.findKthLargest(a, 1))

    # print(s.patition(a, 0, len(a) - 1))
