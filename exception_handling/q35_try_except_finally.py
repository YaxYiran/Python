# 35. Demonstrate the use of try, except, and finally.

try:
    number = int(input("Enter a number: "))
    print("Number:", number)
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("This block always executes.")
