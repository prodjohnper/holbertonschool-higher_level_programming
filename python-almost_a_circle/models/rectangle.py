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
        self.validator('width', width)
        self.validator('height', height)
        self.validator('x', x)
        self.validator('y', y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def validator(self, attr, value):
        '''
            Validator function
        '''
        if type(value) is not int:
            raise TypeError(f'{attr} must be an integer')
        else:
            if attr == 'width' or attr == 'height':
                if value <= 0:
                    raise ValueError(f'{attr} must be > 0')
            else:
                if value < 0:
                    raise ValueError(f'{attr} must be >= 0')

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
        self.validator('width', value)
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
        self.validator('height', value)
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
        self.validator('x', value)
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
        self.validator('y', value)
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

    def update(self, *args, **kwargs):
        '''
            Assigns args to attrs, acception both positional and keyword args
        '''
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for index, arg in enumerate(args):
                setattr(self, attrs[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
