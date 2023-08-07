# 28438 행렬 연산 (행렬 계산하기)

from sys import stdin, stdout
from itertools import product

input = stdin.readline
print = stdout.write

N, M, Q = map(int, input().split(" "))
row_delta = [0] * N
col_delta = [0] * M
matrix = [[0] * M for _ in range(N)]
for _ in range(Q):
    operator, order, value = map(int, input().split(" "))
    if operator == 1:
        row_delta[order - 1] += value
    if operator == 2:
        col_delta[order - 1] += value
for r, c in product(range(N), range(M)):
    matrix[r][c] = row_delta[r] + col_delta[c]
for matrix_sub in matrix:
    print(f"{' '.join(map(str, matrix_sub))}\n")