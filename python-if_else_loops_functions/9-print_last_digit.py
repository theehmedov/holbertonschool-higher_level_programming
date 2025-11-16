#!/usr/bin/python3
# this is a comment
def print_last_digit(number):
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
