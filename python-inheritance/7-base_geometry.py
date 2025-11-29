#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
It serves as a base class for geometry with centralized validation logic.
"""


class BaseGeometry:
    """
    A class that defines the base geometry.
    """

    def area(self):
        """
        Raises an Exception because area() is not implemented yet.

        Raises:
            Exception: Always, with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value (used in error messages).
            value (int): The value to verify.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        # 1. Type Check: Must be strictly an integer (no booleans, no floats)
        # Note: type(value) is strictly used here to avoid bools being ints
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        # 2. Value Check: Must be positive
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
