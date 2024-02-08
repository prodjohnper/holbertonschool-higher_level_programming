#!/usr/bin/python3
'''
    6-base_geometry.py
    Description: Public instance method: def integer_validator
    (self, name, value): that validates value.
'''


class BaseGeometry:
    '''
        Public instance method: def integer_validator(self, name, value):
        that validates value. '''

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
