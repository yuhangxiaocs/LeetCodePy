class Solution(object):
    '''
        python的set是hash set
    '''

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        num_set = set(nums)
        max_length = -1
        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                cur_len = 1

                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_len += 1

                max_length = max(max_length, cur_len)
        return max_length


if __name__ == '__main__':
    test = [1, 2, 3, 4, 6]

    print(Solution().longestConsecutive(test))
