#!/usr/bin/python3
"""This module defines a Rectangle class with width, height, area, perimeter,
string representation using '#' character, eval-able __repr__,
__del__ method, and number_of_instances tracking.
"""


class Rectangle:
    """Defines a rectangle with width and height."""

    number_of_instances = 0  # public class attribute

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1  # increment on new instance

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle with '#' characters."""
        if self.__width == 0 or self.
