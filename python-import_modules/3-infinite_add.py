#!/usr/bin/python3
import sys


def infinite_add(*args):
    return sum(map(int, args))


if __name__ == "__main__":
    arguments = sys.argv[1:]
    total = infinite_add(*arguments)
    print(total)
