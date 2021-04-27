#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        negnum = number * -1
        dig = negnum % 10
        print("{:d}".format(dig), end="")
        return(dig)
    elif number == 0:
        print("{:d}".format(0), end="")
        return(0)
    else:
        dig = number % 10
        print("{:d}".format(dig), end="")
        return(dig)
