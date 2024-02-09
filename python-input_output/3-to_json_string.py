#!/usr/bin/python3
import json

'''
    3-to_json_string.py
    Description: Write a function that returns the
    JSON representation of an object (string)
'''


def to_json_string(my_obj):
    ''' Write a function that returns the JSON
        representation of an object (string)
    '''
    return json.dumps(my_obj)
