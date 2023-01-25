import sys


def add(a, b):
    print(a + b)


if __name__ == '__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    add(a, b)
