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
