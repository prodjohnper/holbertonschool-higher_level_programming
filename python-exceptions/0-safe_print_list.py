#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for _ in range(x):
            print('{}'.format(my_list[_]), end='')
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
