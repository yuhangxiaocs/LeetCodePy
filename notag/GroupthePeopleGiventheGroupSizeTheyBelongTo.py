# 就是先看有多少类 把类相同的放到一起处理

class Solution:
    def groupThePeople(self, groupSizes):
        # 用{}创建一个空字典
        A = {}
        for i, size in enumerate(groupSizes):
            if size not in A:
                A[size] = []
            A[size].append(i)
        res = []
        print(A)
        for size in A:
            for i in range(0, len(A[size]), size):
                res.append(A[size][i:i + size])
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
