#!/usr/bin/python3
'''
    square.py
    Description: Class Square that
    inherits from class Rectangle
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        Class Square that inherits from class Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
            Class Constructor
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
            Square instance string representation
        '''
        id = self.id
        x = self.x
        y = self.y
        s = self.width

        return f'[Square] ({id}) {x}/{y} - {s}'

    @property
    def size(self):
        '''
            Size attribute getter
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
            Size attribute setter
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
            Method that assings attributes
        '''
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for _, arg in enumerate(args):
                setattr(self, attrs[_], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
            Returns dictionary representation of a Square
        '''
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
