#!/usr/bin/python3
def safe_print_list(my_list=[], x = 0):
    new_list = []
    for count, item in enumerate(my_list):
        if count == x:
            break
        new_list.append(item)
    try:
        for x in new_list:
            print("{}".format(x), end="")
        print("")
        if count < x:
            raise my_Error
        return x
    except:
        return count + 1
