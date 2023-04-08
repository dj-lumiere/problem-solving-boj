# 2164 카드2

from collections import deque

N = int(input())
card_deque = deque([i for i in range(1, N + 1)])
for i in range(N - 1):
    card_deque.popleft()
    card_deque.append(card_deque.popleft())
print(*card_deque)
