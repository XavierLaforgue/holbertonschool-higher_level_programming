#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
	message = "is positive"
elif number == 0:
	message = "is zero"
elif number < 0:
	message = "is negative"
else:
	message = "is not a number"
print(f"{number} {message}")
