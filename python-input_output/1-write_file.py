#!/usr/bin/python3
'''
    1-write_file.py
    Description: Write a function that writes a string to a text
    file (UTF8) and returns the number of characters written
'''


def write_file(filename="", text=""):
    ''' Function that writes a string to a text file,
        returns the number of characters written
    '''
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(text)
    return len(text)
