#!/usr/bin/python3
"""
1-my_list.py: Defines a class MyList that inherits from list and adds
a method to print a sorted version of the list.
"""


class MyList(list):
    """
    Inherits from list and provides a public instance method
    to print the list elements in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        Assumes all elements are of type int.
        """
        # sorted(self) returns a *new* sorted list, which is then printed.
        print(sorted(self))
