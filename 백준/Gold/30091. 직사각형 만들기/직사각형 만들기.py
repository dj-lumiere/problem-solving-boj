# 30091 직사각형 만들기

from itertools import combinations
from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
L = list(map(int, input().split(" ")))
perimeter_area_dict = {}
for i, j in combinations(range(N), 2):
    perimeter = 2 * (L[i] + L[j])
    if perimeter not in perimeter_area_dict:
        checked = [False] * N
        checked[i] = True
        checked[j] = True
        perimeter_area_dict[perimeter] = [L[i] * L[j], checked]
    else:
        area, checked = perimeter_area_dict[perimeter]
        if not any((checked[i], checked[j])):
            checked[i] = True
            checked[j] = True
            area += L[i] * L[j]
        perimeter_area_dict[perimeter] = [area, checked]
result = 0
for k, (area, checked) in perimeter_area_dict.items():
    result = max(area, result)
print(result)