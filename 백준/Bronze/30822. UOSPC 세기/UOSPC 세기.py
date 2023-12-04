# 30822 UOSPC 세기

from collections import Counter

n = int(input())
word = input()
letter_count = Counter(word)
for letter in "uospc":
    if letter not in letter_count:
        letter_count[letter] = 0
print(min(letter_count[letter] for letter in "uospc"))