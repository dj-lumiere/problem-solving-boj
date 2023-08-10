# 14289 본대 산책 3

# 인접 행렬의 거듭제곱에 대한 문제.

NO_PATH = 0
HAS_PATH = 1
MOD = 1_000_000_007
adjacent_matrix = [[]]


# 8*8 행렬 곱셈 정의
def matrix_multiply(
    matrix1: list[list[int]], matrix2: list[list[int]]
) -> list[list[int]]:
    N = len(matrix1)
    new_matrix = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            new_matrix_element = 0
            for k in range(N):
                new_matrix_element += matrix1[i][k] * matrix2[k][j]
            if new_matrix_element >= 0:
                new_matrix[i][j] = new_matrix_element % MOD
            else:
                new_matrix[i][j] = -1 * ((-1 * new_matrix_element) % MOD)
    return new_matrix


# 8*8 행렬 제곱 정의
def matrix_square(matrix: list[list[int]]) -> list[list[int]]:
    return matrix_multiply(matrix, matrix)


def sol(matrix: list[list[int]], index: int) -> int:
    # A**(2**n)에 대한 행렬을 세팅해두기
    N = len(matrix)
    matrix_powered_dict = dict()
    matrix_powered_dict[0] = matrix
    for i in range(32):
        matrix_powered_dict[i + 1] = matrix_square(matrix_powered_dict[i])
    binary_index = [index // (2**i) % 2 for i in range(32)]
    # 8*8 단위 행렬 세팅
    final_matrix = [[1 if i == j else 0 for i in range(N)] for j in range(N)]
    # binary_index의 원소 중 1인 것들만 곱하기
    for k, j in enumerate(binary_index):
        if j:
            final_matrix = matrix_multiply(final_matrix, matrix_powered_dict[k])
    return final_matrix[0][0]


N, M = map(int, input().split(" "))
adjacent_matrix = [[NO_PATH] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split(" "))
    adjacent_matrix[a - 1][b - 1] = adjacent_matrix[b - 1][a - 1] = HAS_PATH
D = int(input())
print(sol(adjacent_matrix, D))