
from collections import Counter

text = input("Enter your text: ")

words = text.lower().split()

characters = [char for char in text if not char.isspace()]

word_count = Counter(words)
char_count = Counter(characters)

print("\n===== Text Analyzer =====")

print("Total words:", len(words))
print("Total characters:", len(characters))

if char_count:
    print("Most frequent character:", char_count.most_common(1)[0][0])

if word_count:
    print("Most frequent word:", word_count.most_common(1)[0][0])

print("\nWord repetitions:")
for word, count in word_count.items():
    print(word, ":", count)

print("\nCharacter repetitions:")
for char, count in char_count.items():
    print(repr(char), ":", count)
