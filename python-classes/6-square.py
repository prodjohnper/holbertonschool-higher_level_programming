#!/usr/bin/python3
''' Write a class Square that defines a square.
'''


class Square:
    ''' Class Square definition.
'''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        ''' Retrieve the value of __size '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Property setter '''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        ''' Retrieve the value of __position '''
        return self.__position

    @position.setter
    def position(self, value):
        if (
            type(value) is not tuple or
            len(value) is not 2 or
            type(value[0]) is not int or
            type(value[1]) is not int or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        ''' Access side value stored in __size '''
        side = self.__size
        ''' Calculate square area '''
        result = side * side

        return result

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
