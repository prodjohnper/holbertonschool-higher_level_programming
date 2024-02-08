#!/usr/bin/python3
'''
    9-rectangle.py

    Description: Write a class Square(based on 9-rectangle.py)
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
        Class Square that inherits from Rectangle
    '''

    def __init__(self, size):
        super().integer_validator('size', size)
        super().__init__(size, size)
