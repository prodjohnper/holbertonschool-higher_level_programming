#!/usr/bin/python3
def uppercase(str):

    uppercase_list = [chr(ord(char) - 32) if 97 <= ord(char) <= 122
                      else char for char in str]
    result = ''.join(uppercase_list)

    print(result)
