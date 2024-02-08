#!/usr/bin/python3
'''
    0-read_file.py
    Description: Write a function that reads a
    text file (UTF8) and prints it to stdout
'''


def read_file(filename=""):
    '''
        Function that reads a text file (UTF8) and prints it to stdout
    '''
    with open(filename, encoding="UTF-8") as f:
        read_data = f.read()

    print(read_data, end='')
