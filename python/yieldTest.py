import itertools

'''
    一个带有 yield 的函数就是一个 generator，它和普通函数不同，
    生成一个 generator 看起来像函数调用，但不会执行任何函数代码，
    直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
    虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，
    并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
    看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
'''


def fab(maxx):
    n, a, b = 0, 0, 1
    while n < maxx:
        yield b
        a, b = b, a + b
        n += 1


for i in fab(5):
    print(i)

print()
it = fab(5)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())


# 最后一个next就会抛出异常 在循环中会自动处理异常
# print(it.__next__())

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def add_child(self, node):
        self._children.append(node)

    # 转换成解释器读取的格式
    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    # 这里使用的是迭代器代理 只要将序列通过这个函数返回即可 它自动有next等方法
    def __iter__(self):
        return self._children


root = Node(0)
node1 = Node(1)
node2 = Node(2)

root.add_child(node1)
root.add_child(node2)

for child in root._children:
    print(child, end=' ')
print()


# # # # # # # # # # # # # # # # # # # # # # # # # #
# 迭代器切片
def count(n):
    while True:
        yield n
        n += 1


c = count(0)

for i in itertools.islice(c, 10, 20):
    print(i, end=' ')
print()
for p in itertools.permutations(['a', 'b', 'c']):
    print(list(p))

for p in itertools.combinations([['1', '2'], 'b', 'c'], 3):
    print("combination:", end=' ')
    print(p)
