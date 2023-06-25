# 28255 3단 초콜릿 아이스크림
from math import ceil
from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def rev(target: str) -> str:
    return target[::-1]


def tail(target: str) -> str:
    return target[1:]


def find_prefix(target: str) -> str:
    prefix_length = ceil(len(target) / 3)
    prefix = target[:prefix_length]
    return prefix


def triple_icecream_check(test_string: str) -> int:
    test_prefix = find_prefix(test_string)
    if test_string == test_prefix + rev(test_prefix) + test_prefix:
        return 1
    elif test_string == test_prefix + tail(rev(test_prefix)) + test_prefix:
        return 1
    elif test_string == test_prefix + rev(test_prefix) + tail(test_prefix):
        return 1
    elif test_string == test_prefix + tail(rev(test_prefix)) + tail(test_prefix):
        return 1
    return 0


T = int(input())
for _ in range(T):
    test_sequence = input().strip()
    print(f"{triple_icecream_check(test_sequence)}\n")