# H번 - 탭 UI

from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
tab_length = [0] + [int(input()) * 2 for _ in range(N)]
total_tab_length = sum(tab_length)
center_position = [0]
for i, v in enumerate(tab_length):
    if i == 0:
        continue
    center_position.append(center_position[-1] + v)
for i, v in enumerate(center_position):
    center_position[i] = v - tab_length[i] // 2
window_length = int(input()) * 2
Q = int(input())
for _ in range(Q):
    i = int(input())
    window_position = center_position[i] - window_length // 2
    if total_tab_length < window_length:
        window_position = 0
    elif window_position < 0:
        window_position = 0
    elif window_position + window_length >= total_tab_length:
        window_position = total_tab_length - window_length
    print(f"{window_position/2:0.2f}")