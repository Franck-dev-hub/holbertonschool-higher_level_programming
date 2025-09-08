#!/usr/bin/python3

def safe_print_integer(value):
    try:
        int(value)
        print("{}".format(value))
        return True
    except ValueError:
        print("{} is not an integer".format(value))
        return False
