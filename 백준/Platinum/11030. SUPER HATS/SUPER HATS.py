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
start = 10**8
while start % 5 == 0:
    eulerphi[start] = start * 4 // 10
    start = start * 4 // 10
while start % 2 == 0:
    eulerphi[start] = start // 2
    start = start // 2
a, b = map(int, input().split(" "))
does_not_exceed_100000000_special = {(2, 3), (2, 4)}
if (
    a == 1
    or b == 1
    or (b == 2 and a <= 10**4)
    or (a, b) in does_not_exceed_100000000_special
):
    print(power_tower(eulerphi, [a] * b, 10**8))
else:
    print(f"{power_tower(eulerphi,[a]*b,10**8)%10**8:0>8}")