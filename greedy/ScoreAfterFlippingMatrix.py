class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        row, col = len(A), len(A[0])

        for line in A:
            if line[0] == 0:
                for i in range(len(line)):
                    line[i] = 1 - line[i]

        # 这以后 每一列开头都是1了
        res = len(A) * 2 ** (col - 1)

        for j in range(1, col):
            tmp = 0
            for i in range(row):
                if A[i][j] == 1:
                    tmp += 1

            res += max(tmp, row - tmp) * 2 ** (col - j - 1)

        return res
