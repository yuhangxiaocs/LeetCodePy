

def f():
    x = 1

    def g():
        x = 5
        print(x)

    g()


if __name__ == '__main__':
    f()
