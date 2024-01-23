#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def usage_msg():
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    a = int(sys.argv[1])
    operator = str(sys.argv[2])
    b = int(sys.argv[3])

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))
