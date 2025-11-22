#!/usr/bin/python3
import sys

if __name__ == "__main__":
    a = sys.argv[1:]
    b = len(a)
    c = 0
    if l == 1:
        print("0")
    else:
        for i, arg in enumerate(a, start=1):
            c = int(c) + int(arg)
        print(int(c))
