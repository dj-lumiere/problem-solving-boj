# 28126 Space-A

from sys import stdin, stdout
from collections import Counter


def input():
    return stdin.readline().strip()


def is_movable(move_counter: dict[str, int], x: int, y: int) -> bool:
    x -= 1
    y -= 1
    R_count = move_counter["R"]
    U_count = move_counter["U"]
    X_count = move_counter["X"]
    required_X = min(x, y)
    required_U = y - required_X
    required_R = x - required_X
    if U_count < required_U or R_count < required_R:
        offset = min(required_R, required_U, X_count)
        required_R -= offset
        required_U -= offset
        required_X += offset
    if X_count < required_X:
        offset = required_X - X_count
        required_X -= offset
        required_U += offset
        required_R += offset
    if X_count >= required_X and U_count >= required_U and R_count >= required_R:
        return True
    return False


N = int(input())
moves = list(input().strip())
move_counter = Counter(moves)
M = int(input())
answer = 0
for _ in range(M):
    if is_movable(move_counter, *map(int, input().split(" "))):
        answer += 1
print(f"{answer}")