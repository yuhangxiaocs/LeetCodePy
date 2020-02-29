class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(start, k, n, path):

            if k == 0:
                if n == 0:
                    res.append(path[:])
                return

            for i in range(start, 10):
                if n - i < 0: break

                path.append(i)
                dfs(i + 1, k - 1, n - i, path)
                path.pop()

        dfs(1, k, n, [])
        return res


if __name__ == '__main__':
    print(Solution().combinationSum3(3, 7))
