# 18115 카드 놓기

from collections import deque

N = int(input())
card_initial = deque(range(1, N + 1))
current_card = deque()
commands = list(map(int, input().split()))
for command in commands:
    if command == 1:
        current_card.appendleft(card_initial.popleft())
    if command == 2:
        tmp = card_initial.popleft()
        current_card.appendleft(card_initial.popleft())
        card_initial.appendleft(tmp)
    if command == 3:
        current_card.appendleft(card_initial.pop())
result = [0] * N
for i, v in enumerate(current_card, start=1):
    result[v - 1] = i
print(*result)