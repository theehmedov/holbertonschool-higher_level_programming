#!/usr/bin/python3
import sys

if __name__ == "__main__":
    a = len(sys.argv) - 1
    if a == 1:
        print(f"{a} argument:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
    elif a == 0:
        print(f"{a} arguments.")
    else:
        print(f"{a} arguments:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
