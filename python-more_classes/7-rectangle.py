#!/usr/bin/python3
"""
    5-rectangle.py

    Description: Print the message Bye 'rectangle...'.
"""


class Rectangle:
    """ Returns public class attribute number_of_instances """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        symbol = (str(self.print_symbol) * self.__width + '\n') * self.__height
        if self.width == 0 or self.height == 0:
            return ''
        return symbol.strip()

    def __repr__(self) -> str:
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(Self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
