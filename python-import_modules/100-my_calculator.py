#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

argc = len(sys.argv)

if argc != 4:
    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    exit(1)

operator = str(sys.argv[2])
a = int(sys.argv[1])
b = int(sys.argv[3])

if operator == '+':
    result = add(a, b)
elif operator == '-':
    result = sub(a, b)
elif operator == '*':
    result = mul(a, b)
elif operator == '/':
    result = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

print('{} {} {} = {}'.format(a, operator, b, result))
