# 17372 피보나치 수의 최대공약수의 합

PRECOMPUTE_LIMIT = 100000
MOD = 10**9 + 7


def precompute_phi(phi_sum):
    for i in range(1, PRECOMPUTE_LIMIT):
        phi_sum[i] += i
        j = 2
        while j * i < PRECOMPUTE_LIMIT:
            phi_sum[j * i] -= phi_sum[i]
            j += 1
        phi_sum[i] += phi_sum[i - 1]


def euler_phi_sum(N: int) -> int:
    if N in phi_sum:
        return phi_sum[N]
    result = N * (N + 1) // 2
    i = 2
    while i <= N:
        j = N // (N // i)
        result -= (j - i + 1) * euler_phi_sum(N // i)
        i = j + 1
    phi_sum[N] = result
    return result


def matrix_multiply(
    matrix1: list[list[int]], matrix2: list[list[int]]
) -> list[list[int]]:
    new_matrix = [[0 for i in range(2)] for i in range(2)]
    for i in range(2):
        for j in range(2):
            new_matrix[i][j] = (
                sum(matrix1[i][k] * matrix2[k][j] for k in range(2)) % MOD
            )
    return new_matrix


def matrix_square(matrix: list[list[int]]) -> list[list[int]]:
    return matrix_multiply(matrix, matrix)


def fib(index: int) -> int:
    binary_index = [index // (2**i) % 2 for i in range(64)]
    # 2*2 단위 행렬 세팅
    final_matrix = [[1 if i == j else 0 for i in range(2)] for j in range(2)]

    # binary_index의 원소 중 1인 것들만 곱하기
    for i, j in enumerate(binary_index):
        if j:
            final_matrix = matrix_multiply(final_matrix, matrix_powered_dict[i])
    return final_matrix[1][0]


def fib_sum(A, B):
    return (fib(B + 2) - fib(A + 1)) % MOD


fib_matrix = [[1, 1], [1, 0]]
matrix_powered_dict = dict()
matrix_powered_dict[0] = fib_matrix
for i in range(64):
    matrix_powered_dict[i + 1] = matrix_square(matrix_powered_dict[i])
phi_sum = {i: 0 for i in range(PRECOMPUTE_LIMIT)}
precompute_phi(phi_sum)
N = int(input())
n_over_d_possible_values = []
for i in range(1, int(N**0.5) + 1):
    if i == N // i:
        n_over_d_possible_values.append(i)
    else:
        n_over_d_possible_values.extend([i, N // i])
n_over_d_possible_values.sort()
n_over_d_lower_limit = [N // i for i in n_over_d_possible_values]
n_over_d_phi_sum = [euler_phi_sum(i) for i in n_over_d_possible_values]
n_over_d_as_gcd_count = [2 * i - 1 for i in reversed(n_over_d_phi_sum)]
n_over_d_fib_sum = []
for i, v in enumerate(n_over_d_possible_values):
    if i == 0:
        n_over_d_fib_sum.append(1)
        continue
    n_over_d_fib_sum.append(
        fib_sum(n_over_d_possible_values[i - 1] + 1, n_over_d_possible_values[i])
    )
print(sum(i * j for i, j in zip(n_over_d_as_gcd_count, n_over_d_fib_sum)) % MOD)