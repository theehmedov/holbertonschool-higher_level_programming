#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Represents a list with an extra method to print it sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
