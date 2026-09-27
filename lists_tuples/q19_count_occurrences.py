# 19. Count the occurrences of an element in a list.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
element = int(input("Enter the element to count: "))

count = 0

for number in numbers:
    if number == element:
        count += 1

print("Occurrences:", count)
