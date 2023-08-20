# 12446 バクテリアの増殖 (Large)
from sys import stdin


def input():
    return stdin.readline().strip()


def precompute_euler_phi(limit: int, eulerphi: list[int]):
    prime_flags = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit**0.5) + 1):
        if not prime_flags[i]:
            continue
        prime_flags[i * 2 : limit + 1 : i] = [False] * (limit // i - 1)
    for i in range(2, limit + 1):
        if not prime_flags[i]:
            continue
        for j in range(i, limit + 1, i):
            eulerphi[j] *= i - 1
            eulerphi[j] //= i


def find_maximum_depth(eulerphi: list[int], B: int, C: int) -> tuple[list[int], int]:
    euler_phi_list = [0] * B
    euler_phi_list[0] = C
    maximum_step = B - 1
    for j in range(1, B):
        euler_phi_list[j] = eulerphi[euler_phi_list[j - 1]]
        if euler_phi_list[j] == 1:
            maximum_step = j - 1
            break
    return euler_phi_list[: maximum_step + 1], maximum_step + 1


def calculate(eulerphi: list[int], A: int, B: int, C: int) -> int:
    mod_c_list, maximum_step = find_maximum_depth(eulerphi, B, C)
    mod_c_list.append(1)
    maximum_step += 1
    dp = [[0] * min(i, maximum_step) for i in range(1, B + 1)]
    is_excessive = [[True] * min(i, maximum_step) for i in range(1, B + 1)]
    dp[-1] = [pow(A, A, mod_c_list[i]) for i in range(maximum_step)]
    if A <= 4:
        is_excessive[-1] = [
            A**A >= mod_c_list[i] for i in range(len(is_excessive[-1]))
        ]
    if A == 2 and B >= 2:
        is_excessive[-2] = [256 >= mod_c_list[i] for i in range(len(is_excessive[-2]))]
    for j in range(-2, -B - 1, -1):
        for k in range(min(len(dp[j]), maximum_step - 1)):
            dp[j][k] = pow(
                dp[j + 1][k],
                dp[j + 1][k + 1] + mod_c_list[k + 1] * is_excessive[j + 1][k + 1],
                mod_c_list[k],
            )
    return dp[0][0]


eulerphi = [i for i in range(1001)]
precompute_euler_phi(1000, eulerphi)
N = int(input())
for i in range(1, N + 1):
    A, B, C = map(int, input().split(" "))
    result = calculate(eulerphi, A, B, C)
    print(f"Case #{i}: {result}")