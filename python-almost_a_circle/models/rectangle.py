#!/usr/bin/python3
'''
    rectangle.py
    Description: Class Rectangle
    that inherits from Base
'''
from models.base import Base


class Rectangle(Base):
    '''
        Class Rectangle that inherits from Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            Class constructor
        '''
        super().__init__(id)  # Call superclass const with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
            Width attribute getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Width attribute setter
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
            Height attribute getter
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Height attribute setter
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
            X attribute getter
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            X attribute setter
        '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
            Y attribute getter
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            Y attribute setter
        '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
            Calculate and return rectangle area
        '''
        return self.width * self.height

    def display(self):
        '''
            Print rectangle instance with '#'
        '''
        # Move to the starting y coordinate
        for _ in range(self.y):
            print()

        # Print the rectangle lines with '#' and proper indentation
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        '''
            Rectangle instance string representation
        '''
        id = self.id
        w = self.width
        h = self.height
        x = self.x
        y = self.y

        return '[Rectangle] ({}) {}/{} - {}/{}'.format(id, x, y, w, h)

    def update(self, *args):
        '''
            Assigns args to each attr in specified order
        '''
        attrs = ['id', 'width', 'height', 'x', 'y']
        for index, arg in enumerate(args):
            setattr(self, attrs[index], arg)
