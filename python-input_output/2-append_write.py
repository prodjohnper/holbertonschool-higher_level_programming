#!/usr/bin/python3
'''
    2-append_write.py
    Description: Write a function that appends a string at the end of
    a text file (UTF8) and returns the number of characters added
'''


def append_write(filename="", text=""):
    ''' Write a function that appends a string at the end of a
        text file (UTF8) and returns the number of characters added
    '''
    with open(filename, 'a', encoding="UTF-8") as f:
        f.write(text)
    return len(text)
