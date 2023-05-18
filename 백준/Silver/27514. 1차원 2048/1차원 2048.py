# B1번 - 1차원 2048

from collections import Counter

N: int = int(input())
A: list[int] = list(map(int, input().split(" ")))
A_counter: Counter = Counter(A)
A_counter_list = [A_counter[2**i] for i in range(63)]
last_valid_number: int = 0

for i, j in enumerate(A_counter_list):
    if i != 62:
        if j == 0:
            continue
        if j == 1:
            last_valid_number = 2**i
        else:
            A_counter_list[i], A_counter_list[i + 1] = (
                A_counter_list[i] % 2,
                A_counter_list[i] // 2 + A_counter_list[i + 1],
            )
    elif i == 62 and j > 0:
        last_valid_number = 2**62
print(last_valid_number)
