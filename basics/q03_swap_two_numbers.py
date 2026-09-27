# 3. Swap two numbers without using a third variable.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("First number:", a)
print("Second number:", b)
