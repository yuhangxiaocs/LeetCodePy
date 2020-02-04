class Solution(object):

    # Manacher 99.34% 33.33%
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = '#' + "#".join(s) + '#'
        n = len(s)
        p = [0] * n

        # 初始化 其实只要R初始对了就行了
        C, R, rad = 0, -1, 0
        for i in range(n):
            if i <= R:
                rad = min(p[2 * C - i], R - i)

            while i + rad + 1 < n and i - rad - 1 >= 0 and s[i + rad + 1] == s[i - rad - 1]:
                rad += 1

            p[i] = rad

            if i + rad > R:
                R, C = i + rad, i

        res = 0
        for i in range(n):
            # 奇数偶数分开处理
            if i & 1:
                res += (p[i] + 1) // 2
            else:
                res += p[i] // 2

        return res


if __name__ == '__main__':
    s = Solution()

    print(s.countSubstrings("xiao"))
