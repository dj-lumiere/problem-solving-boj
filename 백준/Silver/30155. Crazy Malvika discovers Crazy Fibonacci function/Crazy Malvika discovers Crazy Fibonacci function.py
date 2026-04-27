# 30155 Crazy Malvika discovers Crazy Fibonacci function

from itertools import product
from sys import stdin


def input():
    return stdin.readline().strip()


def matrix_multiply(
    matrix1: list[list[int]], matrix2: list[list[int]]
) -> list[list[int]]:
    new_matrix = [[0 for i in range(2)] for i in range(2)]
    for i, j in product(range(2), repeat=2):
        new_matrix[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(2)) % MOD
    return new_matrix


def matrix_square(matrix: list[list[int]]) -> list[list[int]]:
    return matrix_multiply(matrix, matrix)


def sol(index: int, A: int, B: int) -> int:
    binary_index = [index // (2**i) % 2 for i in range(64)]
    final_matrix = [[1 if i == j else 0 for i in range(2)] for j in range(2)]
    for i, j in enumerate(binary_index):
        if j:
            final_matrix = matrix_multiply(final_matrix, matrix_powered_dict[i])
    return (final_matrix[1][0] * B + final_matrix[1][1] * A) % MOD


MOD = 10**9 + 7
matrix = [[1, 1000000006], [1, 0]]
matrix_powered_dict = dict()
matrix_powered_dict[0] = matrix
for i in range(32):
    matrix_powered_dict[i + 1] = matrix_square(matrix_powered_dict[i])
T = int(input())
for _ in range(T):
    A, B, N = map(int, input().split(" "))
    print(sol(N - 1, A, B))