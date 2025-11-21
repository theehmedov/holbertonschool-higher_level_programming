#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 1:
        print("1 argument:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
    elif argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} arguments:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
