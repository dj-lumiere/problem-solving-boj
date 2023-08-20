# 12446 バクテリアの増殖 (Large)
from sys import stdin


def input():
    return stdin.readline().strip()


def compute_euler_phi(limit: int) -> list[int]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    phi_values = [i for i in range(limit + 1)]

    for i in range(2, limit + 1):
        if not is_prime[i]:
            continue
        for j in range(i, limit + 1, i):
            is_prime[j] = False
            phi_values[j] = (phi_values[j] * (i - 1)) // i
    return phi_values


def find_max_depth(phi_values: list[int], B: int, C: int) -> tuple[list[int], int]:
    euler_phi_list = [C]
    for _ in range(1, B):
        next_value = phi_values[euler_phi_list[-1]]
        euler_phi_list.append(next_value)
        if next_value == 1:
            break
    return euler_phi_list, len(euler_phi_list)


def is_exceeding_threshold(base: int, index: int, threshold: int) -> bool:
    result = 1
    while index:
        if index & 1:
            result *= base
        base *= base
        index >>= 1
        if result >= threshold:
            return False
    return True


def calculate(phi_values: list[int], A: int, B: int, C: int) -> int:
    mod_c_list, max_step = find_max_depth(phi_values, B, C)
    dp = [[0] * min(i, max_step) for i in range(1, B + 1)]
    excessive_checks = [[True] * min(i, max_step) for i in range(1, B + 1)]

    dp[-1] = [pow(A, A, mod_c_list[i]) for i in range(max_step)]

    if A <= 4:
        excessive_checks[-1] = [
            not is_exceeding_threshold(A, A, mod_c_list[i])
            for i in range(len(excessive_checks[-1]))
        ]

    if A == 2 and B >= 2:
        excessive_checks[-2] = [
            not is_exceeding_threshold(A, A, mod_c_list[i])
            for i in range(len(excessive_checks[-2]))
        ]

    for j in range(-2, -B - 1, -1):
        for k in range(min(len(dp[j]), max_step - 1)):
            dp[j][k] = pow(
                dp[j + 1][k],
                dp[j + 1][k + 1] + mod_c_list[k + 1] * excessive_checks[j + 1][k + 1],
                mod_c_list[k],
            )
    return dp[0][0]


phi_values = compute_euler_phi(1000)
N = int(input())
for i in range(1, N + 1):
    A, B, C = map(int, input().split(" "))
    result = calculate(phi_values, A, B, C)
    print(f"Case #{i}: {result}")
