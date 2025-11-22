#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= a:
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
