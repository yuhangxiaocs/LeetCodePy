class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(start, n, k, path, res):

            if k == 0:
                res.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                dfs(i + 1, n, k - 1, path, res)
                path.pop()

        dfs(1, n, k, [], res)

        return res


print(Solution().combine(4, 2))
