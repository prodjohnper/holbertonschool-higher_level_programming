#!/usr/bin/python3
"""
    8-rectangle.py

    Description: Print the message Bye 'rectangle...'.
"""


class Rectangle:
    """ Static method def bigger_or_equal(rect_1, rect_2): that returns the
        biggest rectangle based on the area
    """

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
            raise ValueError('width must be >= 0')
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

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            if rect_1.area() == rect_2.area():
                rect_1
            else:
                return rect_1 if rect_1.area() > rect_2.area() else rect_2
