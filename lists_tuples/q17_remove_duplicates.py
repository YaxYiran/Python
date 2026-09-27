# 17. Remove duplicate elements from a list.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print("List without duplicates:", unique)
