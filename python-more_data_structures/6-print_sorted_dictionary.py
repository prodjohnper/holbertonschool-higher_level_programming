#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    srtd_dict = sorted(a_dictionary)

    for key in srtd_dict:
        print('{}: {}'.format(key, a_dictionary[key]))
