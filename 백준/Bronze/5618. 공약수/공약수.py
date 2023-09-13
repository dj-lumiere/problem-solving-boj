# 5618 공약수
from math import gcd


def divisors(target):
    target_divisors = []

    for i in range(1, int(target**0.5) + 1):
        if target % i:
            continue
        target_divisors.extend([i, target // i])

    target_divisors = list(set(target_divisors))
    target_divisors.sort()
    return target_divisors


N = int(input())
numbers = list(map(int, input().split(" ")))
print(*divisors(gcd(*numbers)), sep="\n")