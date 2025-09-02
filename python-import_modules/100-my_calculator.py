#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b> ")
        exit(1)

    a = int(argv[1])
    ope = argv[2]
    b = int(argv[3])

    if ope == '+':
        result = add(a, b)
    elif ope == '-':
        result = sub(a, b)
    elif ope == '*':
        result = mul(a, b)
    elif ope == '/':
        result = float(div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, ope, b, result))


if __name__ == "__main__":
    main()
