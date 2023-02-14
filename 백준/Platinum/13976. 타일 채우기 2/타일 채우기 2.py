# 13976 타일 채우기 2

N = int(input())
mod = 1000000007
# 2*2 행렬 곱셈 정의
def matrix_multiply(
    matrix1: list[list[int]], matrix2: list[list[int]]
) -> list[list[int]]:
    new_matrix = [[0 for i in range(2)] for i in range(2)]
    for i in range(2):
        for j in range(2):
            new_matrix_element = 0
            for k in range(2):
                new_matrix_element += matrix1[i][k] * matrix2[k][j]
            if new_matrix_element >= 0:
                new_matrix[i][j] = new_matrix_element % mod
            else:
                new_matrix[i][j] = -1 * ((-1 * new_matrix_element) % mod)
    return new_matrix


# 2*2 행렬 제곱 정의
def matrix_square(matrix: list[list[int]]) -> list[list[int]]:
    return matrix_multiply(matrix, matrix)

if N % 2:
    print(0)
else:
    N //= 2
    # a(0) = 1, S(1) = 3
    # a(n+2) = 3*a(n+1)+2*S(n)
    # a(n+2) = 4*a(n+1)-a(n)
    matrix = [[4, -1], [1, 0]]
    # A**(2**n)에 대한 행렬을 세팅해두기
    matrix_powered_dict = dict()
    matrix_powered_dict[0] = matrix
    initial_matrix = [3, 1]
    for i in range(64):
        matrix_powered_dict[i + 1] = matrix_square(matrix_powered_dict[i])
    binary_index = [(N-1) // (2**i) % 2 for i in range(64)]
    # 2*2 단위 행렬 세팅
    final_matrix = [[1 if i == j else 0 for i in range(2)] for j in range(2)]
    # binary_index의 원소 중 1인 것들만 곱하기
    for k, j in enumerate(binary_index):
        if j:
            final_matrix = matrix_multiply(final_matrix, matrix_powered_dict[k])
    # 마지막으로 [3, 1] 곱하기
    final_value_list = [0, 0]
    for k in range(2):
        for j in range(2):
            final_value_list[j] += final_matrix[j][k] * initial_matrix[k]
    # b**n이 0<b**n<1이므로, c(n)-1이 정수부가 된다.
    result = final_value_list[0] % mod
    print(result)