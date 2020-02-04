class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n // 2):
            m = n - 2 * i
            print(m)
            print(i, i + m - 1)
            # 要加偏移量
            shif = i
            for j in range(i, i + m - 1):
                matrix[i + shif][j + shif], matrix[j + shif][m - 1 - i + shif], matrix[m - 1 - i + shif][
                    m - 1 - j + shif], matrix[m - 1 - j + shif][i + shif] = \
                    matrix[m - 1 - j + shif][i + shif], matrix[i + shif][j + shif], matrix[j + shif][m - 1 - i + shif], \
                    matrix[m - 1 - i + shif][m - 1 - j + shif]
            for m in matrix:
                print(m)
        return matrix


if __name__ == '__main__':
    grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    for i in grid:
        print(i)
    print()
    s = Solution()

    matrix = s.rotate(grid)

    # for i in matrix:
    #     print(i)
