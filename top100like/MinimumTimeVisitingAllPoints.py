class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        costs = 0

        # for i in range(len(points) - 1):
        #     # x = min(abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1]), )
        #     y = max(abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1]))
        #     print(y)
        #     costs += y
        #
        # return costs

        # 一行代码谁不会呢！
        # 这题是greedy方法
        return sum([max(abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1]))
                    for i in range(len(points) - 1)])


if __name__ == '__main__':
    x = Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]])
    print(x)
