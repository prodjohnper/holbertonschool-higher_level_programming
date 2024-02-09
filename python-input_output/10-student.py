#!/usr/bin/python3
'''
    10-student.py
    Description: Define a class Student that defines
    a student by first_name, last_name, and age.
'''


class Student:
    ''' class Student that defines a student
        by first name, last name and age
    '''

    def __init__(self, first_name, last_name, age):
        '''
            Instantiation with first_name, last_name and age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
            Retrieves a dictionary representation of a Student instance
        '''
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
