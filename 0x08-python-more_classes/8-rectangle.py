#!/usr/bin/python3
"""Defines a class"""


class Rectangle:
    """A class Rectangle

    Attributes:
        number_of_instance (int): The number of rectangle instances.
        print_symbol (any type): Symbol to print
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Creates an instance of class Rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                [rec.append(str(self.print_symbol))
                    for j in range(self.__width)]
                if i != self.__height - 1:
                    rec.append('\n')
            return ("".join(rec))

    def __repr__(self):
        """Return a string representation of a rectangle syntax."""
        rec_repr = "Rectangle(" + str(self.__width)
        rec_repr += ', ' + str(self.__height) + ')'
        return rec_repr

    def __del__(self):
        """Deletes a Rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): The first Rectangle
            rect_2 (Rectangle): The second Rectangle

        Returns:
            The biggest rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("ract_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("ract_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
