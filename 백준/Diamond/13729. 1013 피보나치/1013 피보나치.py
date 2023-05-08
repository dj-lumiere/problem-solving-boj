# 13729 1013 피보나치


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
            if new_matrix_element >= 0:
                new_matrix[i][j] = new_matrix_element % mod
            else:
                new_matrix[i][j] = -1 * ((-1 * new_matrix_element) % mod)
    return new_matrix


# 2*2 행렬 제곱 정의
def matrix_square(matrix: list[list[int]], mod: int) -> list[list[int]]:
    return matrix_multiply(matrix, matrix, mod)


def fib_matrix(index: int, mod: int) -> int:
    # A**(2**n)에 대한 행렬을 세팅해두기
    matrix_powered_dict = dict()
    matrix_powered_dict[0] = [[1, 1], [1, 0]]
    initial_matrix = [1, 0]
    max_digit_in_binary = index.bit_length()
    for i in range(max_digit_in_binary):
        matrix_powered_dict[i + 1] = matrix_square(matrix_powered_dict[i], mod)
    binary_index = [index // (2**i) % 2 for i in range(max_digit_in_binary)]
    # 2*2 단위 행렬 세팅
    final_matrix = [[1 if i == j else 0 for i in range(2)] for j in range(2)]
    # binary_index의 원소 중 1인 것들만 곱하기
    for k, j in enumerate(binary_index):
        if j:
            final_matrix = matrix_multiply(final_matrix, matrix_powered_dict[k], mod)
    return final_matrix[1][0]


# 1000으로 나눈 나머지의 피사노 주기가 1500임을 이용
fib = []

fib_mod_dict = {i: [] for i in range(1000)}

for i in range(1500):
    if i < 2:
        fib.append(1)
    else:
        fib.append(sum(fib[-2:]) % 1000)
for index, value in enumerate(fib):
    fib_mod_dict[value].append(index + 1)


n = int(input())
if n == 10**13:
    print(-1)
else:
    i_candidates = [[] for i in range(13 + 1)]
    i_candidates[3] = fib_mod_dict[n % 1000]
    for i in range(4, 13 + 1):
        for j in i_candidates[i - 1]:
            for k in range(10):
                # 10**i의 피사노 주기는 1.5*10**i
                if n % (10**i) == fib_matrix(k * 3 * 10 ** (i - 1) // 2 + j, 10**i):
                    i_candidates[i].append(k * 3 * 10 ** (i - 1) // 2 + j)
    if i_candidates[-1]:
        print(min(i_candidates[-1]))
    else:
        print(-1)