#!/usr/bin/python3
def safe_print_division(a, b):
    print("Inside result:", end=" ")
    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        print(c)
        return c
