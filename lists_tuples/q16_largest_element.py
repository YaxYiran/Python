# 16. Find the largest element in a list.

numbers = list(map(int, input("Enter numbers: ").split()))

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)
