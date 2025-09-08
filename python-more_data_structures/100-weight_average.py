#!/usr/bin/python3

def weight_average(my_list=[]):
    weight = 0
    div = 0
    for key, value in my_list:
        weight += key * value
        div += value
    return weight / div
