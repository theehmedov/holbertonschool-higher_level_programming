#!/usr/bin/python3
"""BaseGeometry class with an unimplemented area method."""


class BaseGeometry:
    """Represent a base geometry."""

    def area(self):
        """Raise an exception indicating that area is not implemented."""
        raise Exception("area() is not implemented")
