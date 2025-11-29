#!/usr/bin/python3
"""Function that returns True if an object is an instance of a subclass
(inherited from) the specified class, otherwise False."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherits from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
