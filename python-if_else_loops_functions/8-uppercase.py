#!/usr/bin/python3
# this is a comment
def uppercase(str):
    for c in str:
        print("{}".format(chr(ord(c) - 32) if 'a' <= c <= 'z' else c), end="")
    print()
