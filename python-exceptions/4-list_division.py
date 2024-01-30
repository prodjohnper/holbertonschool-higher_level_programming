#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_lst = []

    for _ in range(list_length):
        try:
            result = my_list_1[_] / my_list_2[_]

            if my_list_2[_] == 0:
                raise ZeroDivisionError

            result_lst.append(result)
        except ZeroDivisionError:
            print('division by 0')
            result_lst.append(0)
        except (TypeError, ValueError):
            print('wrong type')
            result_lst.append(0)
        except IndexError:
            print('out of range')
            result_lst.append(0)
        finally:
            pass

    return result_lst
