#!/usr/bin/python3
# comment
def pow(a, b):
    c = 1
    for i in range(abs(b)):
        c *= a
    return c if b >= 0 else 1/c
