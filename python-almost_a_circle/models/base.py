#!/usr/bin/python3
'''
    base.py
    Description: This class will be the “base”
    of all other classes in this project
'''
import json


class Base:
    '''
        Manage id attribute in all your future classes
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Assigns the provided id to the instance attribute id, otherwise
            it increments the __nb_objects counter and assigns the new value
            to id '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  # Increment and assign new id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
            Return JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            Write JSON string representation of list_objs to a file
        '''
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]))
