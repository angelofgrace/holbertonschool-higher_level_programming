#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return(None)
    list_truthy = list()
    for x in my_list:
        if x % 2 == 0:
            list_truthy.append(True)
        else:
            list_truthy.append(False)
    return(list_truthy)
