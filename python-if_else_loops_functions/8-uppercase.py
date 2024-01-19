#!/usr/bin/python3
def uppercase(str):
    str_length = len(str)
    upper_chars = ''

    for c in range(0, str_length):
        if ord(str[c]) >= 97 and ord(str[c]) <= 122:
            char = ord(str[c])
            char -= 32
            upper_chars += chr(char)
        else:
            upper_chars += str[c]
    print("{:s}".format(upper_chars))
