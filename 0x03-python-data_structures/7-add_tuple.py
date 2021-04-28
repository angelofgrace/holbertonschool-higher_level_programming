#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        tup_a_1 = tuple_a[0]
        tup_a_2 = tuple_a[1]
    elif len(tuple_a) == 1:
        tup_a_1 = tuple_a[0]
        tup_a_2 = 0
    else:
        tup_a_1 = 0
        tup_a_2 = 0
    if len(tuple_b) >= 2:
        tup_b_1 = tuple_b[0]
        tup_b_2 = tuple_b[1]
    elif len(tuple_b) == 1:
        tup_b_1 = tuple_b[0]
        tup_b_2 = 0
    else:
        tup_b_1 = 0
        tup_b_2 = 0
    newtup = (tup_a_1 + tup_b_1, tup_a_2 + tup_b_2)
    return(newtup)
