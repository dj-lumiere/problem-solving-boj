# 4862 마지막 자리

from sys import stdin


def input():
    return stdin.readline().strip()


def is_excessive(base: int, exp: int, threshold: int):
    result = 1
    while exp:
        if exp & 1:
            result *= base
        if result >= threshold:
            return True
        base *= base
        exp >>= 1
        if exp and base >= threshold:
            return True
    return False


def power_tower(eulerphi: dict[int, int], tower: list[int], MOD: int):
    is_excessive_flag = [True] * (len(tower) - 1)
    if MOD == 1:
        return 1
    euler_phi_list = [1] * len(tower)
    for i in range(len(tower)):
        if i == 0:
            euler_phi_list[i] = MOD
            continue
        if euler_phi_list[i - 1] == 1:
            break
        euler_phi_list[i] = eulerphi[euler_phi_list[i - 1]]
    sub_result = 1
    for i in range(len(tower) - 1, 0, -1):
        if is_excessive(tower[i], sub_result, euler_phi_list[i]):
            break
        sub_result = pow(tower[i], sub_result)
        is_excessive_flag[i - 1] = False
    result = [1 for _ in range(len(tower))]
    result[-1] = tower[-1] % euler_phi_list[-1]
    for i in range(len(tower) - 2, -1, -1):
        if is_excessive_flag[i]:
            result[i] = pow(
                tower[i], result[i + 1] + euler_phi_list[i + 1], euler_phi_list[i]
            )
        else:
            result[i] = pow(tower[i], result[i + 1], euler_phi_list[i])
    # print(result)
    return result[0]


eulerphi = {}
for i in range(1, 7 + 1):
    start = 10**i
    while start % 5 == 0:
        eulerphi[start] = start * 4 // 10
        start = start * 4 // 10
    while start % 2 == 0:
        eulerphi[start] = start // 2
        start = start // 2
while True:
    try:
        b, i, n = [int(input()) for _ in range(3)]
        if i == 0:
            print("0" * (n - 1) + "1")
        else:
            print(f"{power_tower(eulerphi, [b] * i, 10**n):0>7}"[-n:])
    except:
        break