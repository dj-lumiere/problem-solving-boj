# 29159 케이크 두 개

from sys import stdin
from fractions import Fraction


def input():
    return stdin.readline().strip()


def find_center_of_gravity(points: list[tuple[int, int]]) -> tuple[Fraction, Fraction]:
    result_x = [points[i][0] for i in range(4)]
    result_y = [points[i][1] for i in range(4)]
    return (Fraction(sum(result_x), 4), Fraction(sum(result_y), 4))


square_point = []
for _ in range(8):
    x, y = map(int, input().split(" "))
    square_point.append((x, y))

x1, y1 = find_center_of_gravity(square_point[:4])
x2, y2 = find_center_of_gravity(square_point[4:])

# 대각선의 교점을 잇는 직선의 방정식
a = (y2 - y1) / (x2 - x1)
b = y1 - x1 * a
print(a, b)