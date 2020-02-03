class Solution:

    def manacher(self, s):
        s = '#' + "#".join(s) + '#'
        s = list(s)
        n = len(s)

        p = [1] * n

        C, R, rad = 0, -1, 0
        maxR, maxC = -1, -1
        for i in range(n):
            if i <= R:
                rad = min(p[2 * C - i], R - i)

            while i + rad + 1 < n and i - rad - 1 >= 0 and s[i + rad + 1] == s[i - rad - 1]:
                rad += 1

            p[i] = rad

            if i + rad > R:
                R = i + rad
                C = i

                if rad > maxR:
                    maxR = rad
                    maxC = C

        print(s)


if __name__ == '__main__':
    Solution().manacher("xiao")
