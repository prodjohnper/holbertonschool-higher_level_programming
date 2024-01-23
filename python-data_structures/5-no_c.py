#!/usr/bin/python3

def no_c(my_string):

    lst = list(my_string)

    while 'C' in lst:
        lst.remove('C')
    while 'c' in lst:
        lst.remove('c')

    new_string = ''.join(lst)
    return new_string
