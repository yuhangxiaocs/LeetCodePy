import math


class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()

        def check(nums):

            n = len(nums)

            for i in range(n - 1):

                s = (nums[i] + nums[i + 1])

                sqrt = int(math.sqrt(s))
                if s != sqrt ** 2: return False
            return True

        def dfs(nums, pos, path):

            if len(path) >= 2:
                if not check(path): return

            if pos == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == True: continue
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    dfs(nums, pos + 1, path)
                    path.pop()
                    visited[i] = False

        path, res = [], []
        visited = [False for _ in range(len(A))]
        dfs(A, 0, path)
        return len(res)
