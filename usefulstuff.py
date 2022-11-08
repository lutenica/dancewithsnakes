#!/usr/bin/python3
"""
    Some useful functions
"""

def list_shift(list_name, direction, step):
    """
    Shifts list either left or right, with the given step.
    """

    if direction.lower() == 'forward':

        for i in range(0, step):

            list_name.insert(0,list_name.pop())
    else:

        for i in range(0, step):

            list_name.append(list_name.pop(0))

def flatten_list(_list):
    """
    Pass any nested list and flatten it to 1D
    """
    flat_list = []

    for element in _list:

        if isinstance(element, list):
            for item in element:
                flat_list.append(item)

        else:
            flat_list.append(element)

    return flat_list
