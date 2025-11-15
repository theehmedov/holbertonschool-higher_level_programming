#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(" ".join(str.split()[4:6] + str.split()[0:1] + str.split()[6:7]))
