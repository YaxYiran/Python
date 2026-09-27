# 23. Count occurrences of words in a given sentence.

sentence = input("Enter a sentence: ").lower()
words = sentence.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word occurrences:")
for word, count in word_count.items():
    print(word, ":", count)
