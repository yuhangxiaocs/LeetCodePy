'''

    if a[i][j] = 0 set row i and column j all 0s

'''


def setZero(matrix, x, dim=0):
    n = len(matrix)

    for i in range(n):
        if dim == 0:
            matrix[x][i] = 0
        else:
            matrix[i][x] = 0


def setMatrixZero(matrix):
    rows, columns = set(), set()

    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                columns.add(j)

    for row in rows:
        setZero(matrix, row, dim=0)

    for column in columns:
        setZero(matrix, column, dim=1)

    for i in matrix:
        print(i)


if __name__ == '__main__':
    matrix = [[1 for _ in range(5)] for __ in range(5)]

    matrix[0][0] = 0
    matrix[2][2] = 0
    matrix[4][4] = 0

    print(matrix)
    setMatrixZero(matrix)
