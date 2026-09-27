# 25. Check if a key exists in a dictionary.

student = {
    "name": "Jafar",
    "age": 20,
    "course": "Python"
}

key = input("Enter the key to search: ")

if key in student:
    print("Key exists.")
else:
    print("Key does not exist.")
