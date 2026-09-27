# 20. Find the sum of all elements in a tuple.

numbers = tuple(map(int, input("Enter tuple elements separated by spaces: ").split()))

total = 0

for number in numbers:
    total += number

print("Sum:", total)
