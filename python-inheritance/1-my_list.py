#!/usr/bin/python3
'''
    1-my_list.py

    Description: Create a class MyList that inherits from list.
'''


class MyList(list):
    '''
        Class MyList that inherits from list
    '''

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
