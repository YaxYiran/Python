# 24. Find the intersection of two sets.

set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

print("Intersection:", set1 & set2)
