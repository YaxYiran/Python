# 27. Remove all special characters from a string.

text = input("Enter a string: ")
result = ""

for character in text:
    if character.isalnum() or character == " ":
        result += character

print(result)
