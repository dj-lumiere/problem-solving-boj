# 28066 타노스는 요세푸스가 밉다

from collections import deque
from sys import stdin, stdout


input = stdin.readline
print = stdout.write

N, K = map(int, input().split(" "))
my_deque = deque(list(range(1, N + 1)))
while len(my_deque) >= 1:
    my_deque.rotate(-1)
    if len(my_deque) < K:
        print(f"{my_deque[-1]}")
        break
    for _ in range(K - 1):
        my_deque.popleft()