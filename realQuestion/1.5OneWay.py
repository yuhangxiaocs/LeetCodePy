'''
    transform stringA to stringB using insert, remove, replace in one step, if can, output True, else False

    就是编辑距离问题，采用动态规划
'''


def check(before, after):
    x, y = len(before) + 1, len(after) + 1

    dp = [[0 for i in range(y)] for j in range(x)]
    # init
    for i in range(x): dp[i][0] = i
    for i in range(y): dp[0][i] = i

    for i in range(1, x):
        for j in range(1, y):
            if before[i - 1] == after[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min([dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]])

    for i in dp:
        print(i)
    return dp[x - 1][y - 1] <= 1


if __name__ == '__main__':
    print(check("ad", "ad"))
    # dp = [[0] * 3] * 4
    # dp[0][0] = 1
    # dp[0][0] = 2
    # dp[0][0] = 3
    #
    # dp[1][1] = 100
    #
    # print(dp)
