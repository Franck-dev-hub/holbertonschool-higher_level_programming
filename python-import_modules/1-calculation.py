#!/usr/bin/python3

from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5

    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
    result = sub(a, b)
    print("{} - {} = {}".format(a, b, result))
    result = mul(a, b)
    print("{} * {} = {}".format(a, b, result))
    result = div(a, b)
    print("{} / {} = {}".format(a, b, result))


if __name__ == "__main__":
    main()
