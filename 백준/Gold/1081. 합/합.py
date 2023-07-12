# 1081 합

from itertools import product
from math import log10, floor


def digit_length(target: int) -> int:
    return floor(log10(target)) + 1


def find_ith_digit(end: int, digit_pos: int) -> int:
    return (end // (10 ** (digit_pos - 1))) % 10


def find_count(end: int, digit_pos: int, target: int) -> int:
    digit = find_ith_digit(end, digit_pos)
    result = end // (10**digit_pos) * (10 ** (digit_pos - 1))
    if target < digit:
        result += 10 ** (digit_pos - 1)
    elif target == digit:
        result += end % (10 ** (digit_pos - 1)) + 1
    return result


def number_frequency(end: int):
    num_list = [0 for i in range(10)]
    if end == 0:
        return num_list
    digit = digit_length(end)
    for i, j in product(range(1, digit + 1), range(10)):
        num_list[j] += find_count(end, i, j)
    for i in range(digit):
        num_list[0] -= 10**i
    return num_list


L, U = map(int, input().split(" "))
U_list = number_frequency(U)
L_list = number_frequency(max(0, L - 1))
print(sum((i - j) * k for k, (i, j) in enumerate(zip(U_list, L_list))))