# 18. Find the second largest element in a list.

numbers = list(map(int, input("Enter numbers: ").split()))

numbers.sort()

print("Second largest:", numbers[-2])
