#!/usr/bin/python3
"""Defines a class"""


class Rectangle:
    """A class Rectangle"""

    def __init__(self, width=0, height=0):
        """Creates an instance of class Rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns a rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a Retangle instance."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print the rectangle with the character '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rec = []
            for i in range(self.__height):
                [rec.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    rec.append('\n')
            return ("".join(rec))
