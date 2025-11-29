#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initialize a new Rectangle with width and height.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
