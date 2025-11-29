#!/usr/bin/python3
"""Function that returns True if an object is an instance of, or
inherits from, the specified class."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or its subclass."""
    return isinstance(obj, a_class)
