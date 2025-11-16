#!/usr/bin/python3
# this is a comment
for i in range(10):
    for j in range(10):
        if i < j:
            sep = ", " if not (i == 8 and j == 9) else "\n"
            print("{}{}".format(i, j), end=sep)
