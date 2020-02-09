class Solution(object):

    def find(self, nums, lo, hi, res):
        if lo >= hi: return

        mid = (lo + hi) // 2
        self.find(nums, lo, mid, res)
        self.find(nums, mid + 1, hi, res)

        a = nums[lo:mid + 1]
        b = nums[mid + 1:hi + 1]

        a.append(float('inf'))
        b.append(float('inf'))

        k = lo
        i = j = 0

        while k <= hi:
            if a[i] <= b[j]:
                nums[k] = a[i]
                i += 1
            else:
                nums[k] = b[j]
                if i < len(a) - 1 and j < len(b) - 1:
                    res[0] = min(res[0], i + lo)
                    res[1] = max(res[1], j + mid + 1)
                j += 1

            k += 1

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [999999, -99999999]
        self.find(nums, 0, len(nums) - 1, res)
        print(res[0], res[1])

        return res[1] - res[0] + 1 if res[0] < res[1] else 0


if __name__ == '__main__':
    obj = Solution()
    a = [1, 2, 3, 4]
    print(obj.findUnsortedSubarray(a))
    print(a)
