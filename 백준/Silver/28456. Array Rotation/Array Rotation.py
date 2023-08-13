# 28456 Array Rotation
from itertools import product


def query_1(array: list[list[list[int]]], toggle: bool, row_number: int):
    for i, j in product(range(N), range(N)):
        if i == row_number:
            array[not toggle][i][(j + 1) % N] = array[toggle][i][j]
        else:
            array[not toggle][i][j] = array[toggle][i][j]


def query_2(array: list[list[list[int]]], toggle: bool):
    for i, j in product(range(N), range(N)):
        array[not toggle][j][-i - 1] = array[toggle][i][j]


N = int(input())
array: list[list[list[int]]] = [
    [list(map(int, input().split(" "))) for _ in range(N)],
    [[0] * N for _ in range(N)],
]
Q = int(input())
toggle: bool = False
for _ in range(Q):
    operator, *operand = list(map(int, input().split(" ")))
    if operator == 1:
        query_1(array, toggle, operand[0] - 1)
        toggle ^= True
    if operator == 2:
        query_2(array, toggle)
        toggle ^= True
for i in range(N):
    print(*array[toggle][i])