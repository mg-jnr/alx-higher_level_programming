import random
number = random.randint(-10000, 10000)
if number < 0:
    lastDigit = (number * -1) % 10
    print(f"Last digit of {number} is {lastDigit * -1} and \
is less than 6 and not 0")
elif number >= 0:
    lastDigit = number % 10
    if lastDigit > 5:
        print(f"Last digit of {number} is {lastDigit} and is greater than 5")
    elif lastDigit == 0:
        print(f"Last digit of {number} is {lastDigit} and is 0")
    else:
        print(f"Last digit of {number} is {lastDigit} and \
is less than 6 and not 0")