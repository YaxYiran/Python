# 24. Find the intersection of two sets.

set1 = set(map(int, input("Enter elements of first set: ").split()))
set2 = set(map(int, input("Enter elements of second set: ").split()))

intersection = set1.intersection(set2)

print("Intersection:", intersection)
