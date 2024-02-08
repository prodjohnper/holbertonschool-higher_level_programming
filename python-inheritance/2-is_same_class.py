#!/usr/bin/python3
'''
    2-is_same_class.py
    Description: Function that returns True if the object is exactly an
    instance of the specified class ; otherwise, it returns False.
'''


def is_same_class(obj, a_class):
    '''
        Function that returns True if the object is exactly an instance
        of the specified class ; otherwise it returns False. '''

    return type(obj) == a_class
