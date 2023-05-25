# 1490 자리수로 나누기

from math import gcd, lcm
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

def crt(mod_list: list[int], residue_list: list[int]) -> int:
    if len(mod_list) == 1 and len(residue_list) == 1:
        return residue_list[0] % mod_list[0]
    all_lcm = lcm(*mod_list)
    result = 0
    for i, j in zip(mod_list, residue_list):
        result += j * (all_lcm // i) * pow((all_lcm // i), -1, i)
    return result % all_lcm


def parse_mod_tester(digit_list: list[str]) -> list[int]:
    digits = set([int(i) for i in digit_list if int(i)])
    mod_test = []
    if 8 in digits:
        mod_test.append(8)
    elif 4 in digits:
        mod_test.append(4)
    elif 2 in digits or 6 in digits:
        mod_test.append(2)
    if 9 in digits:
        mod_test.append(9)
    elif 3 in digits or 6 in digits:
        mod_test.append(3)
    if 5 in digits:
        mod_test.append(5)
    if 7 in digits:
        mod_test.append(7)
    return mod_test


def solution(mod_test: list[int], target_number: int) -> int:
    if not mod_test:
        return target_number
    test_value = target_number
    digits = 0
    residue = [(mod - (test_value % mod)) % mod for mod in mod_test]
    if all((i == 0 for i in residue)):
        return test_value
    while True:
        test_value *= 10
        digits += 1
        residue = [(mod - (test_value % mod)) % mod for mod in mod_test]
        offset = crt(mod_test, residue)
        if offset < 10**digits:
            return test_value + offset


N = input().strip()
mod_test = parse_mod_tester(list(N))
print(f"{solution(mod_test, int(N))}")