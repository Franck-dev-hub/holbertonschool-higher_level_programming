#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight = 0
    div = 0
    for key, value in my_list:
        weight += key * value
        div += value
    return weight / div
