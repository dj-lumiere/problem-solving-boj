# 1283 단축키 지정
from copy import copy

N = int(input())
memo = [False] * 26

for _ in range(N):
    string_list = list(map(list, input().split(" ")))
    string_list_total = []
    capital_checker = False
    for i, j in enumerate(string_list):
        next_letter = ord(j[0]) - ord("A")
        if next_letter >= 26:
            next_letter = ord(j[0]) - ord("a")
        if not memo[next_letter]:
            memo[next_letter] = True
            string_list[i][0] = f"[{j[0]}]"
            capital_checker = True
            break
    for i, j in enumerate(string_list):
        string_list_total += j
        string_list_total += [" "]
    string_list_total.pop()
    if not capital_checker:
        for i, j in enumerate(string_list_total):
            if j == " ":
                continue
            next_letter = ord(j[0]) - ord("A")
            if next_letter >= 26:
                next_letter = ord(j[0]) - ord("a")
            if next_letter >= 0 and not memo[next_letter]:
                memo[next_letter] = True
                string_list_total[i] = f"[{j}]"
                break
    print("".join(string_list_total))
