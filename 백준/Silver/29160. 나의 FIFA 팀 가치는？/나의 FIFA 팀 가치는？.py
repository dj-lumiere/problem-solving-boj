# L번 - 나의 FIFA 팀 가치는?

from sys import stdin
from heapq import heappush, heappop


def input():
    return stdin.readline().strip()


N, K = map(int, input().split(" "))
player_value = [[0] for _ in range(12)]
for _ in range(N):
    position, value = map(int, input().split(" "))
    player_value[position].append(-value)
for i in range(1, 11 + 1):
    player_value[i].sort()
selected_player = [0 for _ in range(12)]
for i in range(K):
    for j in range(1, 11 + 1):
        if i != 0:
            heappush(player_value[j], -selected_player[j])
        selected_player[j] = -heappop(player_value[j])
    for j in range(1, 11 + 1):
        if selected_player[j] != 0:
            selected_player[j] -= 1
    for j in range(1, 11 + 1):
        heappush(player_value[j], -selected_player[j])
        selected_player[j] = -heappop(player_value[j])
print(sum(selected_player))