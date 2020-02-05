class Solution(object):
    # 右上角的元素为关键
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        p, q = 0, n - 1

        while p < m and q >= 0:
            if target == matrix[p][q]:
                return True
            elif target < matrix[p][q]:
                q -= 1
            else:
                p += 1

        return False
