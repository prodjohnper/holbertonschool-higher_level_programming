#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    result = []

    for nums in my_list:
        div = (nums % 2 == 0)

        result.append(div)

    return result
