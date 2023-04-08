# 27948 가지 자르기 (FAILED)

# 초기 넓이 S

N, K = map(int, input().split(" "))
mod: int = 1000000007
x_coordinates: list[int] = []
y_coordinates: list[int] = []
for _ in range(N):
    x_coordinate, y_coordinate = map(int, input().split(" "))
    x_coordinates.append(x_coordinate)
    y_coordinates.append(y_coordinate)
half_mod_inv = pow(2, -1, mod)

matrix = [
    [half_mod_inv if j == i % N or j == (i + 1) % N else 0 for j in range(N)]
    for i in range(N)
]

# 행렬의 거듭제곱

# 행렬 곱셈 정의
def linear_combination_matrix_multiply(
    matrix1: list[list[int]], matrix2: list[list[int]]
) -> list[list[int]]:
    new_matrix = [[0 for i in range(N)] for j in range(N)]
    for j in range(N):
        new_matrix[0][j] = (
            sum([matrix1[0][k] * matrix2[k][j] for k in range(N)]) % 1000000007
        )
    for i in range(N):
        for j in range(N):
            new_matrix[i][j] = new_matrix[0][(-i + j) % N]
    return new_matrix

# N*N 행렬 제곱 정의
def linear_combination_matrix_square(matrix: list[list[int]]) -> list[list[int]]:
    return linear_combination_matrix_multiply(matrix, matrix)


# A**(2**n)에 대한 행렬을 세팅해두기
matrix_powered_dict = dict()
matrix_powered_dict[0] = matrix
for i in range(60):
    matrix_powered_dict[i + 1] = linear_combination_matrix_square(
        matrix_powered_dict[i]
    )


def sol(matrix: list[list[int]], index: int, initial_matrix: list[int]) -> list[int]:
    binary_index = [index // (2**i) % 2 for i in range(60)]
    # 2*2 단위 행렬 세팅
    final_matrix = [[1 if i == j else 0 for i in range(N)] for j in range(N)]
    # binary_index의 원소 중 1인 것들만 곱하기
    for k, j in enumerate(binary_index):
        if j:
            final_matrix = linear_combination_matrix_multiply(final_matrix, matrix_powered_dict[k])
    final_value_list = [0 for i in range(N)]
    for k in range(N):
        for j in range(N):
            final_value_list[j] += final_matrix[j][k] * initial_matrix[k]
    return final_value_list


x_coordinates = sol(matrix, K, x_coordinates)
y_coordinates = sol(matrix, K, y_coordinates)
x_coordinates.append(x_coordinates[0])
y_coordinates.append(y_coordinates[0])

S: int = 0
for i in range(N):
    S += (
        x_coordinates[i] * y_coordinates[i + 1]
        - x_coordinates[-i - 1] * y_coordinates[-i - 2]
    )
S = abs(S)

# S * 2**-1 (원래 S를 2로 나누어줘야하는게 정상이었으니 여기서 2의 모듈로 역원을 곱해줌)

answer = S * half_mod_inv % mod
print(answer)
