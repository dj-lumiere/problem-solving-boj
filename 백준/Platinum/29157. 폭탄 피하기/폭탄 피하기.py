# 29157 폭탄 피하기
from sys import stdin


def input():
    return stdin.readline().strip()


def bitmask_to_list(status: int, length: int):
    return [bool(status & 1 << i) for i in range(length)]


MOD = 10**9 + 7
factorial_mod = [1] * 2000001
for i in range(1, 2000000 + 1):
    factorial_mod[i] = factorial_mod[i - 1] * i % MOD
inverse_factorial_mod = [1] * 2000001
inverse_factorial_mod[-1] = pow(factorial_mod[-1], -1, MOD)
for i in range(2000000, 1, -1):
    inverse_factorial_mod[i - 1] = inverse_factorial_mod[i] * i % MOD

N, M, K = map(int, input().split(" "))
result = (
    factorial_mod[N + M] * inverse_factorial_mod[N] * inverse_factorial_mod[M] % MOD
)
bomb_position = [tuple(map(int, input().split(" "))) for _ in range(K)]
bomb_position.sort(key=lambda x: (x[0], x[1]))
for i in range(1, 1 << K):
    contain_list = (
        [(0, 0)]
        + [v1 for v1, v2 in zip(bomb_position, bitmask_to_list(i, K)) if v2]
        + [(N, M)]
    )
    offset = [
        (x2 - x1, y2 - y1) for (x1, y1), (x2, y2) in zip(contain_list, contain_list[1:])
    ]
    invalid_path_flag = False
    for x_diff, y_diff in offset:
        if x_diff < 0 or y_diff < 0:
            invalid_path_flag = True
            break
    if invalid_path_flag:
        continue
    result_sub = 1
    for x_diff, y_diff in offset:
        result_sub *= (
            factorial_mod[x_diff + y_diff]
            * inverse_factorial_mod[x_diff]
            * inverse_factorial_mod[y_diff]
            % MOD
        )
    if len(contain_list) & 1:
        result -= result_sub
        result %= MOD
    else:
        result += result_sub
        result %= MOD
print(result)