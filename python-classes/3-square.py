#!/usr/bin/python3
''' Write a class Square that defines a square.
'''


class Square:
    ''' Class Square definition.
'''

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        ''' Access side value stored in __size '''
        side = self.__size
        ''' Calculate square area '''
        result = side * side

        return result
