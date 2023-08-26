# 27311 치노의 라떼 아트 (Easy)
from sys import stdin
from itertools import product


def input():
    return stdin.readline().strip()


def square_hole_at_edge(x_start, y_start, blank_area_length, latte_pattern):
    blank_sub = 0
    for x, y in product(range(blank_area_length), repeat=2):
        if latte_pattern[y + y_start][x + x_start] != "#":
            continue
        blank_sub += 1
    if not blank_sub:
        return 1
    return 0


def is_heart(latte_pattern, R, C):
    x_max, x_min, y_max, y_min = -1, C, -1, R
    pattern_count = 0
    for x, y in product(range(C), range(R)):
        if latte_pattern[y][x] != "#":
            continue
        x_max = max(x, x_max)
        x_min = min(x, x_min)
        y_max = max(y, y_max)
        y_min = min(y, y_min)
        pattern_count += 1
    if pattern_count == 0:
        return 0
    if x_max - x_min != y_max - y_min:
        return 0
    larger_square_area = (x_max - x_min + 1) * (y_max - y_min + 1)
    blank_area = larger_square_area - pattern_count
    if blank_area == 0:
        return 0
    if int(blank_area**0.5) ** 2 != blank_area:
        return 0
    blank_area_length = int(blank_area**0.5)
    edge = [
        (x_min, y_min),
        (x_min, y_max + 1 - blank_area_length),
        (x_max + 1 - blank_area_length, y_min),
        (x_max + 1 - blank_area_length, y_max + 1 - blank_area_length),
    ]
    if (
        sum(
            square_hole_at_edge(x_start, y_start, blank_area_length, latte_pattern)
            for x_start, y_start in edge
        )
        == 1
    ):
        return 1
    return 0


N = int(input())
for _ in range(N):
    R, C = list(map(int, input().split(" ")))
    latte_pattern = [list(input()) for _ in range(R)]
    print(is_heart(latte_pattern, R, C))