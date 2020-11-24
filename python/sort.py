import random

a = [(random.randint(1, 10), random.randint(1, 10)) for i in range(10)]
print(a)

res = sorted(a, cmp=lambda x, y: x[1] - y[1])
print(res)

s = {}
s.values()
