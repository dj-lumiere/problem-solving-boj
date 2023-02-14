# 2023 신기한 소수
from collections import deque

first_digit = [2, 3, 5, 7]
after_digit = [1, 3, 7, 9]

N = int(input())
number_sub = 0
number_queue = deque()
digit = 1
if N == 1:
    print("\n".join(map(str, first_digit)))
else:
    for j in first_digit:
        number_queue.append((1, j))
    while number_queue:
        digit, next_node = number_queue.popleft()
        for i in after_digit:
            next_node = next_node * 10 + i
            composite_indicator = 1
            for i in range(3, int(next_node**0.5) + 1, 2):
                if not next_node % i:
                    composite_indicator = 0
                    break
            if composite_indicator and digit + 1 < N:
                number_queue.append((digit + 1, next_node))
            elif composite_indicator and digit + 1 == N:
                print(next_node)
            next_node //= 10
