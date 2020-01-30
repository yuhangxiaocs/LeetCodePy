class Solution(object):
    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    #     nums = nums1 + nums2
    #     nums.sort()
    #
    #     if len(nums) % 2 == 0:
    #         return (nums[(len(nums) - 1) / 2] + nums[(len(nums)) / 2]) / 2.0
    #     else:
    #         return nums[len(nums) // 2]

    def findMedianSortedArrays(self, nums1, nums2):
        MAX = 9999999999
        MIN = -999999999
        # 一定是对小数组做二分 是为了(x + y + 1) // 2 - partitionX这里不出现负数
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        x, y = len(nums1), len(nums2)
        # partition并不代表元素下标 而是两元素之间的一个划分
        low, high = 0, x

        while low <= high:
            # 对小数组进行二分
            partitionX = (low + high) // 2
            # 如果是x+y是偶数 加1除以二没有影响 如果是奇数+1除以二就导致partitionX + partitionY是一半多一个元素
            partitionY = (x + y + 1) // 2 - partitionX

            # 分别计算两个数组左半边的最大值和右半边的最小值
            # 如果左半边为空 也就是没有元素在它左边 根据划分的含义 partition == 0 此时设置为MIN 表示比右边任何都小
            # 如果右半边为空 表示所有元素都在左边 也就是partition等于x或y 此时设置minRigh为MAX 表示比左边任何都大
            # 这里的边界条件是为了在下面的测试中 不出现特出情况
            maxLeftX = MIN if partitionX == 0 else nums1[partitionX - 1]
            minRightX = MAX if partitionX == x else nums1[partitionX]

            maxLeftY = MIN if partitionY == 0 else nums2[partitionY - 1]
            minRightY = MAX if partitionY == y else nums2[partitionY]

            # 注意这里是交叉的 x的左边最大 小于y的右边最小；y的左边最大小于x的右边最小
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                return max(maxLeftX, maxLeftY)
            # 如果x的左边大了 那就是再从左半边找 设置high为partitionX - 1
            elif maxLeftX > minRightY:
                high = partitionX - 1
            # 如果x的左边小了 就像大的方向去找 设置low为partition + 1 即可
            else:
                low = partitionX + 1


if __name__ == '__main__':
    s = Solution()

    print(s.findMedianSortedArrays([1, 2], [3, 3]))

'''
def findMid(self, nums):
        length = len(nums)
        if length % 2 == 0:
            return (nums[length // 2] + nums[length // 2 - 1]) / 2.0
        else:
            return nums[length // 2]

    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1:
            return self.findMid(nums2)

        if not nums2:
            return self.findMid(nums1)

        m = len(nums1)
        n = len(nums2)
        if m == 1 and n == 1:
            return (nums1[0] + nums2) / 2
        
        mn = m + n
        # 无交集
        if nums2[0] > nums1[-1]:
            return self.findMid(nums1 + nums2)
        if nums2[-1] < nums1[0]:
            return self.findMid(nums2 + nums1)

        # 两者有交集 先交换合并成一种情况
        if nums2[0] >= nums1[0] and nums2[0] <= nums1[-1]:
            pass
        else:
            nums1, nums2, m, n = nums2, nums1, n, m

        if m % 2 == 0 and n % 2 == 0:
            return self.findMedianSortedArrays(nums1[m // 2:], nums2[:n // 2])
        else:
            return self.findMedianSortedArrays(nums1[:m // 2], nums2[n // 2:])
'''
