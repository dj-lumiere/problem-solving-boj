# 5066 The Counting Problem

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


while True:
    a, b = map(int, input().split(" "))
    if not any((a, b)):
        break
    a, b = min(a, b), max(a, b)
    a_freq = number_frequency(a - 1)
    b_freq = number_frequency(b)
    print(*[v1 - v2 for v1, v2 in zip(b_freq, a_freq)])