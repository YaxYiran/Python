# 17. Remove duplicate elements from a list.

numbers = list(map(int, input("Enter numbers: ").split()))

new_list = []

for number in numbers:
    if number not in new_list:
        new_list.append(number)

print("List without duplicates:", new_list)
