#!/usr/bin/python3

def uppercase(str):
    for i in str:
        temp = ord(i)
        if 96 < temp < 123:
            temp -= 32
        print("{:c}".format(temp), end="")
    print()
