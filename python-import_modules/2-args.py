#!/usr/bin/python3
import sys
a = len(sys.argv) - 1
def arg():
for i in range(1, 6):
    print(f"{i}: {sys.argv[i]}")
if a == 1:
    print(f"{a} argument:")
    print(arg())
elif a == 0:
    print(f"{a} arguments.")
else:
    print(f"{a} arguments:")
    print(arg())
if __name__ == "__main__":
