'''

'''


def combination(arr, num=2):
    '''

    :param arr: 给定的数组 长度为N
    :param num: 在N中挑选num个 求组合
    :return:  返回所有组合
    '''

    def dfs(arr, num, start, path, res):

        if num == 0:
            res.append(path[:])
            return

        for i in range(start, len(arr)):
            path.append(arr[i])
            dfs(arr, num - 1, i + 1, path, res)
            path.pop()

    res = []
    dfs(arr, num, 0, [], res)

    print(res)
    return res


if __name__ == '__main__':
    combination([1, 2, 3], 3)
