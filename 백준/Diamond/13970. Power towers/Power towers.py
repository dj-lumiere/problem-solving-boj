# 13970 Power towers
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


def is_excessive(base: int, exp: int, threshold: int):
    result = 1
    while exp:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
        if result >= threshold:
            return True
    return False


def power_tower(eulerphi: list[int], tower: list[int], index: int, MOD: int):
    global is_excessive_at_next
    if MOD == 1:
        return 1
    if len(tower) - index == 1:
        return tower[index]
    euler_phi_mod = eulerphi[MOD]
    sub_result = power_tower(eulerphi, tower, index + 1, euler_phi_mod)
    base, exp = tower[index], sub_result
    if is_excessive_at_next:
        exp += euler_phi_mod
    # print(f"{index=} {MOD=} {tower[index:]=} {base=} {exp=} {is_excessive(base, exp, MOD)=}")
    if not is_excessive_at_next:
        is_excessive_at_next = is_excessive(base, exp, MOD)
    return pow(base, exp, MOD)


eulerphi = [i for i in range(1000001)]
precompute_euler_phi(1000000, eulerphi)
N, M = map(int, input().split(" "))
for _ in range(N):
    _, *tower = map(int, input().split(" "))
    global is_excessive_at_next
    is_excessive_at_next = False
    for i, v in enumerate(tower):
        if v == 1:
            tower = tower[:i]
            break
    print(power_tower(eulerphi, tower, 0, M) % M, end=" ")