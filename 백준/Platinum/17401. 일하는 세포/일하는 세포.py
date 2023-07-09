# 17401 일하는 세포

from sys import stdin, stdout

input = stdin.readline
print = stdout.write


MOD = 1000000007


def matrix_multiply(
    matrix1: list[list[int]], matrix2: list[list[int]], MOD: int
) -> list[list[int]]:
    if len(matrix1) != len(matrix2[0]):
        raise Exception("MatrixMultiplicationError")
    new_matrix_x_size = len(matrix1[0])
    new_matrix_calculation_count = len(matrix1)
    new_matrix_y_size = len(matrix2)
    new_matrix = [
        [0 for i in range(new_matrix_x_size)] for i in range(new_matrix_y_size)
    ]
    for i in range(new_matrix_x_size):
        for j in range(new_matrix_y_size):
            new_matrix_element = 0
            for k in range(new_matrix_calculation_count):
                new_matrix_element += matrix1[i][k] * matrix2[k][j]
            if new_matrix_element >= 0:
                new_matrix[i][j] = new_matrix_element % MOD
            else:
                new_matrix[i][j] = -1 * ((-1 * new_matrix_element) % MOD)
    return new_matrix


def matrix_square(matrix: list[list[int]], MOD) -> list[list[int]]:
    return matrix_multiply(matrix, matrix, MOD)


def matrix_exp(matrix: list[list[int]], index: int, MOD) -> list[list[int]]:
    matrix_powered_dict = dict()
    matrix_powered_dict[0] = matrix
    for i in range(index.bit_length()):
        matrix_powered_dict[i + 1] = matrix_square(matrix_powered_dict[i], MOD)
    binary_index = [index // (2**i) % 2 for i in range(index.bit_length())]
    final_matrix = [
        [1 if i == j else 0 for i in range(len(matrix))] for j in range(len(matrix))
    ]
    for k, j in enumerate(binary_index):
        if j:
            final_matrix = matrix_multiply(final_matrix, matrix_powered_dict[k], MOD)
    return final_matrix


T, N, D = map(int, input().split(" "))
connection_matrices = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(T)]
result_matrix = [[1 if i == j else 0 for i in range(N)] for j in range(N)]
for i in range(T):
    M = int(input())
    for _ in range(M):
        x, y, c = map(int, input().split(" "))
        connection_matrices[i][x - 1][y - 1] = c
for i, v in enumerate(connection_matrices):
    if i == 0:
        continue
    connection_matrices[i] = matrix_multiply(
        connection_matrices[i - 1], connection_matrices[i], MOD
    )
calculation_batches, calculation_leftovers = divmod(D, T)
if calculation_batches and calculation_leftovers:
    result_matrix = matrix_multiply(
        matrix_exp(connection_matrices[-1], calculation_batches, MOD),
        connection_matrices[calculation_leftovers - 1],
        MOD,
    )
elif not calculation_batches and calculation_leftovers:
    result_matrix = connection_matrices[calculation_leftovers - 1]
elif calculation_batches and not calculation_leftovers:
    result_matrix = matrix_exp(connection_matrices[-1], calculation_batches, MOD)
print("\n".join([" ".join(map(str, [i for i in j])) for j in result_matrix]))