# 10854 Divisions

# 약수의 개수 찾기
# 폴라드 로로 소인수분해

from math import gcd
from random import randint
from sys import setrecursionlimit
from collections import Counter

setrecursionlimit(10000)

N = int(input())

# if n < 3,825,123,056,546,413,051, it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, and 23 (from wikipedia)
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def is_prime(n: int):
    # prime_list의 원소들을 미리 소수로 처리
    if n in prime_list:
        return True
    # 1과 짝수는 소수가 아님
    if n == 1 or n % 2 == 0:
        return False
    # (n-1) = 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    y = 1
    # 소수 리스트를 참조하여 소수 판별
    for i in prime_list:
        x = pow(i, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x + 1 != n:
                return False
            x = y
        if y != 1:
            return False
    return True


factors = []

def pollard_rho(n: int) -> int:
    if is_prime(n):
        return n
    if n % 2 == 0:
        return 2
    if n == 1:
        return 1
    x = randint(2, n - 1)
    y = x
    c = randint(1, n - 1)
    d = 1
    while d == 1:
        x = ((x * x) % n + c + n) % n
        y = ((y * y) % n + c + n) % n
        y = ((y * y) % n + c + n) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollard_rho(n)
    if is_prime(d):
        return d
    else:
        return pollard_rho(d)


next_N = N
for i in prime_list:
    while next_N % i == 0:
        factors.append(i)
        next_N //= i
while next_N > 1:
    factor = pollard_rho(next_N)
    factors.append(factor)
    next_N //= factor

factors_dict = Counter(factors)

divisors = 1
for i, j in factors_dict.items():
    divisors *= j + 1
print(divisors)
