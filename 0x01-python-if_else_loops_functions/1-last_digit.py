#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    neg = number * -1
    LD = neg % 10
    print(f"Last digit of {number:d} is {LD * -1} and "
    "is less than 6 and not 0")
elif number == 0 or number > 0:
    LD = number % 10
    if LD > 5:
        print(f"Last digit of {number:d} is {LD} is greater than 5")
    elif LD == 0:
        print(f"Last digit of {number:d} is {LD} and is 0")
    elif LD < 6 and LD != 0:
        print(f"Last digit of {number:d} is {LD} and "
                "is less than 6 and not 0")
