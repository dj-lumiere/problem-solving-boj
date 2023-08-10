# 27435 파도반 수열 2
from itertools import product

# P(N) = P(N-2)+P(N-3), [1,1,1]
MOD = 998244353


def matrix_multiply(
    matrix1: list[list[int]], matrix2: list[list[int]]
) -> list[list[int]]:
    new_matrix = [[0 for i in range(3)] for i in range(3)]
    for i, j in product(range(3), range(3)):
        new_matrix[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(3)) % MOD
    return new_matrix


def matrix_square(matrix: list[list[int]]) -> list[list[int]]:
    return matrix_multiply(matrix, matrix)


def padovan_result(
    index: int,
    matrix: list[list[int]],
    matrix_powered_dict: dict[int, list[list[int]]],
    initial_matrix: list[int],
) -> int:
    binary_index = [index // (2**i) % 2 for i in range(64)]
    final_matrix = [[1 if i == j else 0 for i in range(3)] for j in range(3)]
    for k, j in enumerate(binary_index):
        if not j:
            continue
        final_matrix = matrix_multiply(final_matrix, matrix_powered_dict[k])
    final_value_list = [0, 0, 0]
    final_value_list[j] = sum(final_matrix[j][k] * initial_matrix[k] for k in range(3))
    result = final_value_list[0] % MOD
    return result


matrix = [
    [0, 1, 1],
    [1, 0, 0],
    [0, 1, 0],
]
# A**(2**n)에 대한 행렬을 세팅해두기
matrix_powered_dict = dict()
matrix_powered_dict[0] = matrix
initial_matrix = [0, 1, 0]
for i in range(64):
    matrix_powered_dict[i + 1] = matrix_square(matrix_powered_dict[i])


T = int(input())
for _ in range(T):
    N = int(input())
    print(padovan_result(N, matrix, matrix_powered_dict, initial_matrix))