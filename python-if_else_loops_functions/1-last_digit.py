#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10 if number >= 0 else number % -10
# last = int(str(number)[-1]) if number >= 0 else -int(str(number)[-1])
if last > 5:
    msg = "and is greater than 5"
elif last == 0:
    msg = "and is 0"
elif last < 6:
    msg = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last} {msg}")
