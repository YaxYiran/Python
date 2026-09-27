# 27. Remove all special characters from a string.

text = input("Enter a string: ")
result = ""

for character in text:
    if character.isalnum() or character.isspace():
        result += character

print("String without special characters:", result)
