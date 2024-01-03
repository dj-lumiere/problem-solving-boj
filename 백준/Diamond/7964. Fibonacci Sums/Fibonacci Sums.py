# 7964 Fibonacci Sums
from itertools import zip_longest
from sys import stdin


def input():
    return stdin.readline().strip()


N1, *A1 = list(map(int, input().split(" ")))
N2, *A2 = list(map(int, input().split(" ")))

N = max(N1, N2) + 3
result = [i + j for (i, j) in zip_longest(A1, A2, fillvalue=0)] + [0, 0, 0]

# First stage: Move from right to left, removing 2's
for i in range(len(result) - 3, -1, -1):
    x = result[i]
    if result[i + 1 : i + 4] == [0, 2, 0]:
        result[i : i + 4] = [x + 1, 0, 0, 1]
    elif result[i + 1 : i + 4] == [0, 3, 0]:
        result[i : i + 4] = [x + 1, 0, 1, 1]
    elif result[i + 1 : i + 4] == [1, 2, 0]:
        result[i : i + 4] = [x, 0, 1, 1]
    elif result[i + 1 : i + 4] == [2, 1, 0]:
        result[i : i + 4] = [x, 1, 0, 1]

last_three_sum = result[0] * 1 + result[1] * 2 + result[2] * 3
if last_three_sum == 2:
    result[:3] = [0, 1, 0]
elif last_three_sum == 3:
    result[:3] = [0, 0, 1]
elif last_three_sum == 4:
    result[:3] = [1, 0, 1]
elif last_three_sum == 5:
    result[:3] = [0, 1, 1]
elif last_three_sum == 6:
    result[:3] = [1, 1, 1]

# Second stage: Move from left to right, removing consecutive 1's
for i in range(len(result) - 2):
    if result[i : i + 3] == [1, 1, 0]:
        result[i : i + 3] = [0, 0, 1]

# Third stage: Move from right to left, removing consecutive 1's
for i in range(len(result) - 3, -1, -1):
    if result[i : i + 3] == [1, 1, 0]:
        result[i : i + 3] = [0, 0, 1]

while result and result[-1] == 0:
    result.pop()

if not result:
    result.append(0)

print(len(result), *result)