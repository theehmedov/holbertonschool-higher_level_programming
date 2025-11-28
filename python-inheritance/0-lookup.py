#!/usr/bin/python3
"""Return the list of available attributes and methods of an object."""


def lookup(obj):
    """Return a list of an object's attributes and methods."""
    return dir(obj)
