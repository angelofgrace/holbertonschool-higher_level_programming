#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    new_list = []
    for count, item in enumerate(my_list):
        if count == x:
            break
        new_list.append(item)
    try:
        total = 0
        for x in new_list:
            try:
                total += 1
                print("{:d}".format(x), end="")
            except:
                total -= 1
                pass
        print("")
        if count < x:
            raise my_Error
        return x
    except:
        return total
