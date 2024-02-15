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

    @staticmethod
    def from_json_string(json_string):
        '''
            Return the list of JSON string representation json_string
        '''
        if json_string is None or json_string == '':
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
            Return an instance with all attributes set
        '''
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)  # Create dummy rectangle instance
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)  # Create dummy square instance
        else:
            raise ValueError('Unsupported class type')

        dummy_instance.update(**dictionary)  # Update attr using dict
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''
            Return a list of instances loaded from a file
        '''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                json_data = f.read()
                dictionary_list = cls.from_json_string(json_data)
                instances = [cls.create(**data) for data in dictionary_list]
                return instances
        except FileNotFoundError:
            return []
