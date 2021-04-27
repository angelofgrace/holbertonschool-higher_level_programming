#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = number % 10
if number < 0 and dig != 0:
    neg = number * -1
    dig = neg % 10
    if dig != 0:
        dig = dig * -1
else:
    dig = number % 10
if dig > 5:
    print("Last digit of" " {:d}"
          .format(number) + " is" + " {:d}"
          .format(dig) + " and is greater than 5")
elif dig < 6 and dig != 0:
    print("Last digit of" " {:d}".format(number) + " is" + " {:d}"
          .format(dig) + " and is less than 6 and not 0")
else:
    print("Last digit of" + " {:d}"
          .format(number) + " is" + " {:d}".format(dig) + " and is 0")
