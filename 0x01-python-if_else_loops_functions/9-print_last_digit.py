#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastDigit = (number * -1) % 10
        print(f"{lastDigit}", end='')
    elif number >= 0:
        lastDigit = number % 10
        print(f"{lastDigit}", end='')
    return (lastDigit)
