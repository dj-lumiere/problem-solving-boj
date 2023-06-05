# 12850 본대 산책2

# 인접 행렬의 거듭제곱에 대한 문제.

NO_PATH = 0
HAS_PATH = 1
MOD = 1_000_000_007
# 정보, 전산, 미래, 신양, 한경직, 진리, 학생, 형남
ADJACENT_MATRIX = [
    [  # 정보 : 전산, 미래
        NO_PATH,  # 정보 -> 정보
        HAS_PATH,
        HAS_PATH,
        NO_PATH,
        NO_PATH,
        NO_PATH,
        NO_PATH,
        NO_PATH,
    ],
    [  # 전산 : 정보, 미래, 신양
        HAS_PATH,
        NO_PATH,
        HAS_PATH,
        HAS_PATH,
        NO_PATH,
        NO_PATH,
        NO_PATH,
        NO_PATH,
    ],
    [  # 미래 : 정보, 전산, 신양, 한경직
        HAS_PATH,
        HAS_PATH,
        NO_PATH,
        HAS_PATH,
        HAS_PATH,
        NO_PATH,
        NO_PATH,
        NO_PATH,
    ],
    [  # 신양 : 전산, 미래, 한경직, 진리
        NO_PATH,
        HAS_PATH,
        HAS_PATH,
        NO_PATH,
        HAS_PATH,
        HAS_PATH,
        NO_PATH,
        NO_PATH,
    ],
    [  # 한경직 : 미래, 신양, 진리, 형남
        NO_PATH,
        NO_PATH,
        HAS_PATH,
        HAS_PATH,
        NO_PATH,
        HAS_PATH,
        NO_PATH,
        HAS_PATH,
    ],
    [  # 진리 : 신양, 한경직, 학생
        NO_PATH,
        NO_PATH,
        NO_PATH,
        HAS_PATH,
        HAS_PATH,
        NO_PATH,
        HAS_PATH,
        NO_PATH,
    ],
    [  # 학생 : 진리, 형남
        NO_PATH,
        NO_PATH,
        NO_PATH,
        NO_PATH,
        NO_PATH,
        HAS_PATH,
        NO_PATH,
        HAS_PATH,
    ],
    [  # 형남 : 한경직, 학생
        NO_PATH,
        NO_PATH,
        NO_PATH,
        NO_PATH,
        HAS_PATH,
        NO_PATH,
        HAS_PATH,
        NO_PATH,
    ],
]


# 8*8 행렬 곱셈 정의
def matrix_multiply(
    matrix1: list[list[int]], matrix2: list[list[int]]
) -> list[list[int]]:
    new_matrix = [[0 for i in range(8)] for i in range(8)]
    for i in range(8):
        for j in range(8):
            new_matrix_element = 0
            for k in range(8):
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
    matrix_powered_dict = dict()
    matrix_powered_dict[0] = matrix
    for i in range(32):
        matrix_powered_dict[i + 1] = matrix_square(matrix_powered_dict[i])
    binary_index = [index // (2**i) % 2 for i in range(32)]
    # 8*8 단위 행렬 세팅
    final_matrix = [[1 if i == j else 0 for i in range(8)] for j in range(8)]
    # binary_index의 원소 중 1인 것들만 곱하기
    for k, j in enumerate(binary_index):
        if j:
            final_matrix = matrix_multiply(final_matrix, matrix_powered_dict[k])
    return final_matrix[0][0]


N = int(input())
print(sol(ADJACENT_MATRIX, N))
