#!/usr/bin/python3

from sys import argv

count = 1
argc= len(argv) - 1

if argc == 0:
    print("0 arguments.")
elif argc == 1:
    print("1 argument:")
    print(f"1: {argv[1]}")
else:
    print(f"{argc} arguments:")
    for i in argv[1:]:
        print(f"{count}: {i}")
        count += 1
