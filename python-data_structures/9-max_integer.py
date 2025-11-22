def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_value = my_list[0]
    for max in my_list:
        if max > max_value:
            max_value = max
    return max_value
