# 12925 Numbers

T = int(input())

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
                new_matrix[i][j] = new_matrix_element % 10000
            else:
                new_matrix[i][j] = -1*((-1*new_matrix_element) % 10000)
    return new_matrix


# 2*2 행렬 제곱 정의
def matrix_square(matrix: list[list[int]]) -> list[list[int]]:
    return matrix_multiply(matrix, matrix)


def sol(test_cases: int):
    # let a = 3+sqrt(5), b = 3-sqrt(5)
    # then a+b = 6, ab = 4 => xx-6x+4=0
    # let c(n)=a**n+b**n, then c(n+2)=6c(n+1)-4c(n)
    # c(0) = 2, c(1) = 6
    # c(n) => [[6,-4],[1,0]]**n*[c1,c0]=[c(n+1),c(n)]
    matrix = [[6, -4], [1, 0]]

    # A**(2**n)에 대한 행렬을 세팅해두기
    matrix_powered_dict = dict()
    matrix_powered_dict[0] = matrix
    initial_matrix = [6, 2]
    for i in range(32):
        matrix_powered_dict[i + 1] = matrix_square(matrix_powered_dict[i])
    for i in range(1, test_cases + 1):
        index = int(input())
        binary_index = [index // (2**i) % 2 for i in range(32)]
        # 2*2 단위 행렬 세팅
        final_matrix = [[1 if i == j else 0 for i in range(2)] for j in range(2)]
        # binary_index의 원소 중 1인 것들만 곱하기
        for k, j in enumerate(binary_index):
            if j:
                final_matrix = matrix_multiply(final_matrix, matrix_powered_dict[k])
        # 마지막으로 [6, 2] 곱하기
        final_value_list = [0, 0]
        for k in range(2):
            for j in range(2):
                final_value_list[j] += final_matrix[j][k] * initial_matrix[k]
        # b**n이 0<b**n<1이므로, c(n)-1이 정수부가 된다.
        result = (final_value_list[1] - 1) % 1000
        print(f"Case #{i}: {result:0>3}")
sol(T)