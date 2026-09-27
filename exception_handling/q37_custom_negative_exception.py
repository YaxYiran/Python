# 37. Raise a custom exception if a given number is negative.

class NegativeNumberError(Exception):
    pass


number = int(input("Enter a number: "))

if number < 0:
    raise NegativeNumberError("Number cannot be negative")

print("Number:", number)
