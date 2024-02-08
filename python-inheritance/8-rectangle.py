#!/usr/bin/python3
'''
    8-rectangle.py

    Description: Write a class BaseGeometry(based on 7-base_geometry.py)
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
        Class Rectangle that inherits from BaseGeometry
    '''

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
