# 30090 백신 개발

from itertools import permutations


def latest_discrepancy(word1: str, word2: str):
    tmp = ""
    max_length = 0
    for i, letter in enumerate(word2):
        tmp += letter
        if word1.endswith(tmp):
            max_length = max(max_length, i + 1)
    return max_length


N = int(input())
words = [input() for _ in range(N)]
max_length = 0
for i in range(1, N + 1):
    for word_sublist in permutations(words, i):
        if i == 1:
            max_length = max(max_length, len(word_sublist[0]))
            continue
        result_sub = sum(len(word) for word in word_sublist)
        for j, word in enumerate(word_sublist):
            if j + 1 == i:
                continue
            connectable_letter_length = latest_discrepancy(word, word_sublist[j + 1])
            if not connectable_letter_length:
                break
            result_sub -= latest_discrepancy(word, word_sublist[j + 1])
        else:
            max_length = max(max_length, result_sub)
print(max_length)