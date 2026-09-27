# 37. Raise a custom exception if a given number is negative.

class NegativeNumberError(Exception):
    pass


number = float(input("Enter a number: "))

if number < 0:
    raise NegativeNumberError("Negative numbers are not allowed.")

print("Number:", number)
