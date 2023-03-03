# 2577 숫자의 개수
from collections import Counter

A, B, C = int(input()), int(input()), int(input())
count_list = Counter(str(A * B * C))
for i in range(0, 9 + 1):
    print(count_list[str(i)])