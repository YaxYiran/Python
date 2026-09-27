# 18. Find the second largest element in a list.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

if len(unique) < 2:
    print("A second largest element does not exist.")
else:
    largest = unique[0]
    second_largest = unique[1]

    if second_largest > largest:
        largest, second_largest = second_largest, largest

    for number in unique[2:]:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number

    print("Second largest element:", second_largest)
