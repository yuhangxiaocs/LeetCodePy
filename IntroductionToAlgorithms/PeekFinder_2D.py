'''
    peek finder in 2-D matrix
'''


def peek_finder_2D(mat):
    def find_local_max(col):
        # 记录local maximum的row
        res = 0
        maxx = -float('inf')
        for i in range(m):

            if mat[i][col] > maxx:
                maxx = mat[i][col]
                res = i
        return res

    m, n = len(mat), len(mat[0])

    lo, hi = 0, n - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        row = find_local_max(mid)

        if mid - 1 >= 0 and mat[row][mid - 1] > mat[row][mid]:
            hi = mid - 1
        elif mid + 1 < n and mat[row][mid + 1] > mat[row][mid]:
            lo = mid + 1
        else:
            return [row, mid]


if __name__ == '__main__':
    mat = [
        [10, 8, 10, 10],
        [14, 13, 12, 11],
        [15, 9, 11, 21],
        [16, 17, 19, 20]
    ]

    row, colunm = peek_finder_2D(mat)
    print(row, colunm)
