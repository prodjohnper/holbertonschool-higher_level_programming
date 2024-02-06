#!/usr/bin/python3
"""
    3-rectangle.py

    Description: Write a class Rectangle that defines a rectangle.
"""


class Rectangle:
    """ Returns Rectangle Area, Perimeter and '#' rectangle shape """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >=0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self) -> str:
        rect_str = ''

        if self.width == 0 or self.height == 0:
            return rect_str

        for _ in range(self.height):
            rect_str += '#' * self.width + '\n'
        return rect_str.strip()
