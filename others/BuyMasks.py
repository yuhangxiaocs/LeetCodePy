res = [''] * 10
ans = [0]


def buyMask(day, days, cur, total):
    if day == days:
        if cur == total:
            print(res)
            ans[0] += 1
        return
    if cur >= 1:
        res[day] = 0
        buyMask(day + 1, days, cur - 1, total)
        res[day] = 1
        buyMask(day + 1, days, cur + 2, total)


if __name__ == '__main__':
    buyMask(0, 10, 5, 1)
    print(ans[0])

    print(sum(range(3, 8)))

    # 每次出门采购一次口罩，消耗家里库存1只，每次限购3个，买到，家里库存就多2两个，买不到，就亏一个，某人一共出门10次，初始有5个口罩，最终剩余
    # 1. 10次之后家里有12只，问这其中买到了多少次
    # 2. 求第一问中所有的可能情况，比如['n', 'n', 'n', 'n', 'n', 'n', 'y', 'y', 'y', 'y']就是一种情况
    # 3. 求出10次以后所有可能的库存情况
