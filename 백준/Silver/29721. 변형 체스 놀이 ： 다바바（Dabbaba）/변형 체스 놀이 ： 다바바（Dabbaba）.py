# 29721 변형 체스 놀이 : 다바바(Dabbaba)

from sys import stdin

DELTA = [(-2, 0), (2, 0), (0, -2), (0, 2)]


def input():
    return stdin.readline().strip()


def is_inbound(pos_x, x_size, pos_y, y_size):
    return 0 <= pos_x < x_size and 0 <= pos_y < y_size


available_position = set()
dabbaba_position = set()
N, K = map(int, input().split(" "))
for _ in range(K):
    x, y = map(int, input().split(" "))
    dabbaba_position.add((x - 1, y - 1))
for x, y in dabbaba_position:
    for dx, dy in DELTA:
        nx, ny = x + dx, y + dy
        if not is_inbound(nx, N, ny, N):
            continue
        if (nx, ny) in dabbaba_position:
            continue
        if (nx, ny) in available_position:
            continue
        available_position.add((nx, ny))
print(len(available_position))
