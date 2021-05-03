#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_3 = []
    x = 0
    while x < list_length:
        try:
            c = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            c = 0
            print("division by 0")
        except IndexError:
            c = 0
            print("out of range")
        except TypeError:
            c = 0
            print("wrong type")
        finally:
            list_3.append(c)
            x += 1
    return list_3
