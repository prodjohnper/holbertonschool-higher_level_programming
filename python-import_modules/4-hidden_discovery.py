#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    str_list = dir(hidden_4)

    for _ in range(0, len(str_list)):
        string = str_list[_]
        if string[:2] != "__" != string[-2:]:
            print(string)
