#!/usr/bin/python3
'''
    7-add_item.py
    Description: Write a script that adds all arguments
    to a Python list, and then save them to a file
'''
import json
import sys


def save_to_json_file(my_obj, filename):
    ''' Write a function that writes an Object to a
        text file, using a JSON representation
    '''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    '''
        Function that creates an Object from a “JSON file"
    '''
    with open(filename, 'r') as f:
        return json.load(f)


try:
    obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    obj = []

for _ in sys.argv[1:]:
    obj.append(_)

save_to_json_file(obj, "add_item.json")
