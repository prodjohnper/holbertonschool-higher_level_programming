#!/usr/bin/python3
'''
    9-student.py
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

    def to_join(self):
        '''
            Retrieves a dictionary representation of a Student instance
        '''
        return self.__dict__
