import dis


def f(a, b):
    a, b = b, a


def fx(a, x):
    a[x], a[a[x]] = a[a[x]], a[x]
    return a


if __name__ == '__main__':
    a = [3, 2, 1, 4]
    print(a)
    # index = a[1]
    # a[1], a[index] = a[index], a[1]

    fx(a, 1)
    print(a)
    dis.dis(f)
    print("==============")
    dis.dis(fx)
