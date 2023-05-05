# 10908 Phibonacci


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


n, k = (int(i) for i in input().split(" "))
mod = 10**9 + 7
# 1. P(n) = phi**n = F(n)phi+F(n-1)
# 2. P(n)**k = phi**nk = A*phi**k+B?
# phi**nk=F(nk)*phi+F(nk-1)=A*phi(k)+B=A*(F(k)*phi+F(k-1))+B
# F(nk)*phi+F(nk-1)=A*F(k)*phi+A*F(k-1)+B
# F(nk)=A*F(k), F(nk-1)=A*F(k-1)+B
# 이 때, gcd(F(nk), F(k))=F(gcd(nk, k))=F(k)
A = (
    fib_matrix(n * k, mod) * pow(fib_matrix(k, mod), -1, mod) % mod
    if fib_matrix(k, mod)
    # 그냥 나누려니 분모가 0이어서 곤란한 경우, mod * mod로 나누어 ((a % (p * p)) // p) / ((b % (p * p)) // p)로 회피
    else (fib_matrix(n * k, mod * mod) // mod)
    * pow(fib_matrix(k, mod * mod) // mod, -1, mod)
    % mod
)
B = (fib_matrix(n * k - 1, mod) - A * fib_matrix(k - 1, mod)) % mod
B = (B + mod) % mod
print(A, B)
