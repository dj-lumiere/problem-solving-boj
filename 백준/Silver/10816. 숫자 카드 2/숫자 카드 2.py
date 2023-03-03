# 10815 숫자 카드 2

from collections import Counter

N = int(input())
card_counter = Counter(map(int, input().split(" ")))
M = int(input())
card_check_list = list(map(int, input().split(" ")))
card_check = [0 for i in range(M)]
for i, j in enumerate(card_check_list):
    if card_counter[j]:
        card_check[i] = card_counter[j]
print(*card_check, sep=" ")