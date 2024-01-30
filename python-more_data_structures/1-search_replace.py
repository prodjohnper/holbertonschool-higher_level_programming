#!/usr/bin/python3

def search_replace(my_list, search, replace):
    replaced_lst = list(map(lambda _: replace if search == _ else _, my_list))
    return replaced_lst
