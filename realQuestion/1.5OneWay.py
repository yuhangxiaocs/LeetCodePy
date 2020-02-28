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
    print(dp[x - 1][y - 1])
    return dp[x - 1][y - 1]


def editDistance(before, after):
    mem = {}

    def helper(before, after, l1, l2, mem):
        if not (l1 + 1) or not (l2 + 1):
            mem[l1, l2] = (l1 + 1) or (l2 + 1)
            return mem[l1, l2]

        if (l1, l2) in mem:
            return mem[l1, l2]

        if before[l1] == after[l2]:
            return helper(before, after, l1 - 1, l2 - 1, mem)
        else:
            # replace
            a = helper(before, after, l1 - 1, l2 - 1, mem) + 1
            # delete
            b = helper(before, after, l1 - 1, l2, mem) + 1
            # insert
            c = helper(before, after, l1, l2 - 1, mem) + 1
            mem[l1, l2] = min([a, b, c])
            return mem[l1, l2]

    res = helper(before, after, len(before) - 1, len(after) - 1, mem)
    return res


if __name__ == '__main__':
    before = "sadljfhaklsjdfhkljashdfkjashdfkjlasd"
    after = "abcdsafasdlfhalsdufouyqwerihbklsjvd9847"
    check(before, after)
    editDistance(before, after)
    # dp = [[0] * 3] * 4
    # dp[0][0] = 1
    # dp[0][0] = 2
    # dp[0][0] = 3
    #
    # dp[1][1] = 100
    #
    # print(dp)
