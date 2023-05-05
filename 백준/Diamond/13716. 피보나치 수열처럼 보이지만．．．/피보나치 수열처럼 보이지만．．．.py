# 13716 피보나치 수열처럼 보이지만...


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
    initial_matrix = [2, 1]
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
    return final_matrix[0][0]


mod = 10**9 + 7
nCr_list = [[0 for r in range(40 + 1)] for n in range(40 + 1)]
for n in range(40 + 1):
    for r in range(40 + 1):
        if n < r:
            nCr_list[n][r] = 0
        elif n == 0:
            nCr_list[n][r] = 1
        elif n == r or r == 0:
            nCr_list[n][r] = 1
        else:
            nCr_list[n][r] = (nCr_list[n - 1][r - 1] + nCr_list[n - 1][r]) % mod

n, k = (int(i) for i in input().split(" "))
F_n_plus_1 = fib_matrix(n + 1, mod)
F_n = fib_matrix(n, mod)
# S(n, k) = F(n+1)*n**k+F(n)*(n+1)**k-2*sum([(k-j)%2*kCj*S(n,j) for j in range(k+1)])
# S(n, 0) = F(n+1)+F(n)-2
S = [(F_n + F_n_plus_1 - 2) % mod]
for a in range(1, k + 1):
    S.append(
        (
            F_n_plus_1 * pow(n, a, mod)
            + F_n * pow(n + 1, a, mod)
            - 1
            - 2 * sum([((a - j) % 2) * nCr_list[a][j] * S[j] for j in range(a)])
        )
        % mod
    )
print(S[-1])
