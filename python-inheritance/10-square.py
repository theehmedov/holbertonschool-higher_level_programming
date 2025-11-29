#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): size of the square sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
