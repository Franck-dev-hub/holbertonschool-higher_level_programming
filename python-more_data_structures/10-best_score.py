#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = 0
    name = None
    for key in a_dictionary.keys():
        if best < a_dictionary[key]:
            best = a_dictionary[key]
            name = key
    return name
