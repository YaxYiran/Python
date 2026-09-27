# 23. Count occurrences of words in a given sentence.

sentence = input("Enter a sentence: ").lower()
words = sentence.split()

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word in count:
    print(word, ":", count[word])
