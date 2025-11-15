#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number % 10
b = number % -10
if number > 0:
    if a > 5:
        print(f"Last digit of {number} is {a} and is greater than 5")
    elif a < 6:
        print(f"Last digit of {number} is {a} and is less than 6 and not 0")
    else:
        print(f"Last gigit of {number} is {a} and is 0")
if number < 0:
    if a > 5:
        print(f"Last digit of {number} is {b} and is greater than 5")
    elif a < 6:
        print(f"Last digit of {number} is {b} and is less than 6 and not 0")
    else:
        print(f"Last gigit of {number} is {b} and is 0")
