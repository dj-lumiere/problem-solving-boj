# 20920 영단어 암기는 괴로워
from sys import stdin
from collections import Counter

input = stdin.readline
word_list = []
N, M = map(int, input().strip().split(" "))
for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue
    word_list.append(word)
word_counter = Counter(word_list)
word_position = {}
for i, v in enumerate(word_list):
    if v not in word_position:
        word_position[v] = i
word_list = list(set(word_list))
word_list = sorted(word_list, key=lambda x: (-word_counter[x], -len(x), x))
print(*word_list, sep="\n")