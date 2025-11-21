#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    if a == 1:
        print("1 argument:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
    elif a == 0:
        print("0 arguments.")
    else:
        print(f"{a} arguments:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
