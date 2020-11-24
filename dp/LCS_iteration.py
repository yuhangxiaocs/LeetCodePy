'''
    有了memo的方法，就可以很快的将问题转换成bottom-up问题，也就是自底向上求解；
    以LCS_v1为例：原问题是[1, m] [1, n]
    子问题可能是[2, m][2, n] 或者 [2, m] [4, n]所以这是很多种组合，那么到最后是什么样呢？
    就是到了最右边
'''


def lcs_iteration(s1, s2, par):
    m = len(s1) + 1
    n = len(s2) + 1
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if s1[i - 1] == s2[j - 1]:
                par[i, j] = (i - 1, j - 1)
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                if dp[i][j - 1] >= dp[i - 1][j]:
                    par[i, j] = (i, j - 1)
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
                    par[i, j] = (i - 1, j)

    return dp[m - 1][n - 1]


def print_path(s1, s2, i, j, par):
    if i == 0 or j == 0: return
    newi, newj = par[i, j]
    print_path(s1, s2, newi, newj, par)
    # 根据算法的原理，如果选中某个元素i j那么它上一个位置一定是i-1和j-1
    if newi + 1 == i and newj + 1 == j:
        print(s1[i - 1], "from seq1 where i=", i - 1, ",", "from seq2 where j=", j - 1)


if __name__ == '__main__':
    s1 = "x i  a o"
    s2 = ".xiadevops"
    par = {}  # 用于记录上一步从哪里而来
    print("LCS is :", lcs_iteration(s1, s2, par))
    print_path(s1, s2, len(s1), len(s2), par)
