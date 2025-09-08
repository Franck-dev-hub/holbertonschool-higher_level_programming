#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None

    key_to_del = []
    for key, val in a_dictionary.items():
        if val == value:
            key_to_del.append(key)

    for key in key_to_del:
        del a_dictionary[key]

    return a_dictionary
