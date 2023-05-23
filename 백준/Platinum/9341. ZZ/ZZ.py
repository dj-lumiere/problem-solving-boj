# 9341 ZZ

from sys import stdin, stdout


input = stdin.readline
print = stdout.write


mod = 10**9 + 9

multiplicative_inverse = [1]
for i in range(1, 100 + 1):
    multiplicative_inverse.append(multiplicative_inverse[-1] * pow(i, -1, mod) % mod)

fib_memo = [0, 1, 1]
for _ in range(200):
    fib_memo.append(sum(fib_memo[-2:]) % mod)


# 2*2 행렬 곱셈 정의
def matrix_multiply_with_mod(
    matrix1: list[list[int]], matrix2: list[list[int]], modulo: int
) -> list[list[int]]:
    new_matrix = [[0 for i in range(2)] for i in range(2)]
    for i in range(2):
        for j in range(2):
            new_matrix_element = 0
            for k in range(2):
                new_matrix_element += matrix1[i][k] * matrix2[k][j]
            if new_matrix_element >= 0:
                new_matrix[i][j] = new_matrix_element % modulo
            else:
                new_matrix[i][j] = -1 * ((-1 * new_matrix_element) % modulo)
    return new_matrix


# 2*2 행렬 제곱 정의
def matrix_square_with_mod(matrix: list[list[int]], modulo: int) -> list[list[int]]:
    return matrix_multiply_with_mod(matrix, matrix, modulo)


def fib_with_mod(index: int, modulo: int) -> int:
    matrix = [[1, 1], [1, 0]]
    matrix_powered_dict_size = index.bit_length()
    # A**(2**n)에 대한 행렬을 세팅해두기
    matrix_powered_dict = dict()
    matrix_powered_dict[0] = matrix
    initial_matrix = [1, 0]
    for i in range(matrix_powered_dict_size):
        matrix_powered_dict[i + 1] = matrix_square_with_mod(
            matrix_powered_dict[i], modulo
        )
    binary_index = [index // (2**i) % 2 for i in range(matrix_powered_dict_size)]
    # 2*2 단위 행렬 세팅
    final_matrix = [[1 if i == j else 0 for i in range(2)] for j in range(2)]
    # binary_index의 원소 중 1인 것들만 곱하기
    for k, j in enumerate(binary_index):
        if j:
            final_matrix = matrix_multiply_with_mod(
                final_matrix, matrix_powered_dict[k], modulo
            )
    return final_matrix[1][0]


def nCr_with_mod(n: int, r: int, mod: int) -> int:
    if r < 0:
        return 0
    else:
        denominator = 1
        for i in range(r):
            denominator *= n - i
            denominator %= mod
        return (denominator * multiplicative_inverse[r]) % mod

    
# a의 계수 = fib(d+2*c-1)-sum(F((c-k)*2)*nCr(d+k,k))
# b의 계수 = fib(d+2*c)-sum(F((c-k)*2+1)*nCr(d+k,k))


T = int(input().strip())
for _ in range(T):
    a, b, c, d = map(int, input().strip().split(" "))
    d -= 1
    b_coefficient = (
        fib_with_mod(d + 2 * c, mod)
        - (
            sum(
                [
                    fib_memo[2 * (c - i - 1) + 1] * nCr_with_mod(d + i, i, mod)
                    for i in range(c)
                ]
            )
            % mod
        )
        % mod
    )
    if c == 1:
        a_coefficient = fib_with_mod(d + 1, mod)
    else:
        a_coefficient = (
            fib_with_mod(d + 2 * c - 1, mod)
            - (
                sum(
                    [
                        fib_memo[2 * (c - i - 1)] * nCr_with_mod(d + i, i, mod)
                        for i in range(c - 1)
                    ]
                )
                % mod
            )
            % mod
        )
    answer = (a_coefficient * a + b_coefficient * b) % mod
    print(f"{answer}\n")