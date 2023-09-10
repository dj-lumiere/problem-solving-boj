# 29766 DKSH 찾기

from sys import stdin


def input():
    return stdin.readline().strip()


word = input()
result = 0
for i, v in enumerate(word):
    if i + 4 > len(word):
        break
    if word[i : i + 4] == "DKSH":
        result += 1
print(result)