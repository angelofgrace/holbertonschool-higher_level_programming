#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return(None)
    greatest = my_list[0]
    for x in range(0, len(my_list)):
        if my_list[x] > my_list[x - 1] and my_list[x] > greatest:
            greatest = my_list[x]
    return(greatest)
