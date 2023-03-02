# 1904 01타일

N = int(input())

# 2*2 행렬 곱셈 정의
def matrix_multiply(
    matrix1: list[list[int]], matrix2: list[list[int]], mod: int
) -> list[list[int]]:
    new_matrix = [[0 for i in range(2)] for i in range(2)]
    for i in range(2):
        for j in range(2):
            new_matrix_element = 0
            for k in range(2):
                new_matrix_element += matrix1[i][k] * matrix2[k][j]
            new_matrix[i][j] = new_matrix_element % mod
    return new_matrix


def matrix_pow(
    matrix: list[list[int]], initial_matrix: list[int], index: int, mod: int
) -> int:
    # matrix**n * [F(2), F(1)]=[F(n+2),F(n+1)]
    index -= 1
    binary_index = [index // (2**i) % 2 for i in range(64)]
    # 2*2 단위 행렬 세팅
    final_matrix = [[1 if i == j else 0 for i in range(2)] for j in range(2)]
    # A**(2**n)에 대한 행렬을 세팅해두기
    matrix_powered_dict = dict()
    matrix_powered_dict[0] = matrix
    for i in range(64):
        matrix_powered_dict[i + 1] = matrix_multiply(
            matrix_powered_dict[i], matrix_powered_dict[i], mod
        )
    # binary_index의 원소 중 1인 것들만 곱하기
    for i, j in enumerate(binary_index):
        if j:
            final_matrix = matrix_multiply(final_matrix, matrix_powered_dict[i], mod)
    # 마지막으로 initial_matrix 곱하기
    final_value_list = [0, 0]
    for k in range(2):
        for j in range(2):
            final_value_list[j] += final_matrix[j][k] * initial_matrix[k]
    return final_value_list[1] % mod


if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    print(
        matrix_pow(matrix=[[1, 1], [1, 0]], initial_matrix=[2, 1], index=N, mod=15746)
    )