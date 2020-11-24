class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """

        row = len(rowSum)
        col = len(colSum)

        # init
        res = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(col):
                x = min(rowSum[i], colSum[j])
                rowSum[i] -= x
                colSum[j] -= x
                res[i][j] = x
        return res
