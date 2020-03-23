import math


# 使用生日攻击概率和泰勒公式近似后的hash碰撞概率，d代表hash值取值空间大小，n代表几次操作
def probability(d, n):
    #
    expon = -(n - 1) * n * 1.0 / (2 * d)
    res = 1 - math.exp(expon)
    return res


print(probability(365, 23))
print(probability(365, 50))
print(probability(365, 70))

print(probability(63 ** 3, 10000))
print(probability(2 ** 128, 1e15))
