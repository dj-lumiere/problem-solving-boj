from collections import Counter

n = int(input())
word = list(input())
word_counter = Counter(word)
target = Counter(list("BRONZESILVER"))
answer = min([word_counter[k] // v for k, v in target.items()])
print(answer)