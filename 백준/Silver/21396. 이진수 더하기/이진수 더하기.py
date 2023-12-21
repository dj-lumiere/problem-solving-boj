# 21396 이진수 더하기
from collections import Counter

T = int(input())
for _ in range(T):
    n, x = map(int, input().split(" "))
    numbers = Counter(map(int, input().split(" ")))
    answer1 = 0
    answer2 = 0
    for k, v in numbers.items():
        if k ^ x in numbers and k ^ x != k:
            answer1 += numbers[k ^ x] * v
        elif k ^ x in numbers and k ^ x == k:
            answer2 += v * (v - 1) // 2
    print(answer1 // 2 + answer2)
