import argparse


def add(a, b):
    print(a + b)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    add(args.a, args.b)
