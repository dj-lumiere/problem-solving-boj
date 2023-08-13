# 9519 졸려
from math import ceil, log2


def combine_patterns(pattern1, pattern2):
    return [pattern1[pattern2[i]] for i in range(len(pattern1))]


X = int(input())
word = list(input())
length = len(word)
LOG = ceil(log2(10**9)) + 1
pattern = [[i for i in range(length)] for _ in range(LOG + 1)]
for j in range(length):
    if j & 1:
        pattern[1][j] = pattern[0][-(j // 2) - 1]
    else:
        pattern[1][j] = pattern[0][j // 2]
for i in range(2, LOG + 1):
    pattern[i] = combine_patterns(pattern[i - 1], pattern[i - 1])
final_conversion = [i for i in range(length)]
for i in range(LOG):
    if X & 1:
        final_conversion = combine_patterns(final_conversion, pattern[i + 1])
    X >>= 1
word_after_conversion = ["" for _ in range(length)]
for i, v in enumerate(final_conversion):
    word_after_conversion[v] = word[i]
print(*word_after_conversion, sep="")