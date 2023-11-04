# 5637 가장 긴 단어
from re import split, match

words: list[str] = []
while True:
    sentence_seperate = split("([a-zA-Z-]+)", input())
    words_sub = []
    for substring in sentence_seperate:
        if match("[a-zA-Z-]+", substring):
            words_sub.append(substring)
    words.extend(words_sub)
    if words[-1] == "E-N-D":
        break
words.pop()
max_length = max(map(len, words))
for word in words:
    if len(word) == max_length:
        print(word.lower())
        break
