from collections import Iterable


def flatten(items):
    for x in items:
        if isinstance(x, Iterable):
            yield from flatten(x)
        else:
            yield x


if __name__ == '__main__':
    x = [1, 2, [3, 4, 5, [6, 7]], [8, 9]]

    for i in flatten(x):
        print(i, end=" ")
    print()
