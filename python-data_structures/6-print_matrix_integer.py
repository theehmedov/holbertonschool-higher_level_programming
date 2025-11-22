#!/usr/bin/python3
for row in matrix:
    for idx, val in enumerate(row):
        if idx != len(row) - 1:
            print("{:d}".format(val), end=" ")
        else:
            print("{:d}".format(val), end="")
    print()  # yeni sətr
