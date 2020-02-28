'''

    和那个快速求数组某段长度的和是一直的 先有个 pre_computation 把 sum[i]代表 0-i的sum
    从而 sum(i...j) = sum[j] - sum[i-1]

    这题就是扩展到二维


    Runtime: 72 ms, faster than 98.47% of Python online submissions for Matrix Block Sum.
    Memory Usage: 12.5 MB, less than 100.00% of Python online submissions for Matrix Block Sum.

'''


class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        # print(m, n)

        for i in range(m):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]

        for i in range(n):
            for j in range(1, m):
                mat[j][i] += mat[j - 1][i]
        # for i in range(n):
        #     print(mat[i])

        res = [[0 for _ in range(n)] for __ in range(m)]
        for i in range(m):
            for j in range(n):

                rmax = i + K if i + K < m else m - 1
                cmax = j + K if j + K < n else n - 1

                mi, mid1, mid2 = 0, 0, 0

                if i - K - 1 >= 0 and j - K - 1 >= 0:
                    mi = mat[i - K - 1][j - K - 1]
                if i - K - 1 >= 0:
                    mid2 = mat[i - K - 1][cmax]
                if j - K - 1 >= 0:
                    mid1 = mat[rmax][j - K - 1]

                res[i][j] = mat[rmax][cmax] - mid1 - mid2 + mi

        return res


if __name__ == '__main__':
    mat = Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
    for i in mat:
        print(i)
