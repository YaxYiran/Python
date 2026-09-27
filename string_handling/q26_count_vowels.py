# 26. Count the number of vowels in a given string.

text = input("Enter a string: ")

count = 0

for character in text:
    if character in "aeiouAEIOU":
        count += 1

print("Vowels:", count)
