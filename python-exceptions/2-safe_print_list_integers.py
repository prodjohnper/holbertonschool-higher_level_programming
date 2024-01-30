#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for _ in range(x):
            if type(my_list[_] is int):
                print('{:d}'.format(my_list[_]), end='')
                count += 1
            else:
                continue
        print()
        return count
    except ValueError:
        count = 0
        for _ in my_list:
            if count == x:
                break
            else:
                count += 1
            print()
            return count
