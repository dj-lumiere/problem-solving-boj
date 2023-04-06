# 23362 Rasterized Lines
# x-phi(x) = N

# 밀러 라빈 소수 판별
# 폴라드 로로 소인수분해

from math import gcd
from random import randint
from collections import Counter
from sys import setrecursionlimit

setrecursionlimit(10000)

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]


def miller_rabin_primality_test(n: int) -> bool:
    # 2, 3, 5, 7, 11, 13을 미리 소수로 처리
    if n in prime_list:
        return True
    # 짝수는 소수가 아님
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


def pollard_rho(n: int) -> int:
    if miller_rabin_primality_test(n):
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
    if miller_rabin_primality_test(d):
        return d
    else:
        return pollard_rho(d)


def factorization_pollard_rho(N: int) -> dict[int, int]:
    next_N = N
    factors = []
    for i in prime_list:
        while next_N % i == 0:
            factors.append(i)
            next_N //= i
    while next_N > 1:
        factor = pollard_rho(next_N)
        factors.append(factor)
        next_N //= factor

    return Counter(factors)


def euler_phi(N: int) -> int:
    next_N = N
    factors = []
    for i in prime_list:
        while next_N % i == 0:
            factors.append(i)
            next_N //= i
    while next_N > 1:
        factor = pollard_rho(next_N)
        factors.append(factor)
        next_N //= factor
    factors_dict = Counter(factors)

    factors = list(set(factors))
    euler_phi = N
    for i in factors:
        euler_phi *= i - 1
        euler_phi //= i
    return euler_phi


T = int(input())
for _ in range(T):
    __ = input()
    N = int(input())
    if N == 1:
        print(1)
    else:
        answer = 0
        # gcd(a,b)=1인 거면 a+b=N+1 (a와 b는 서로소여야함)
        # gcd(a,b)=g인 거면 a+b=N+g (g의 배수에 대해 -> N도 g의 배수여야함)
        # 약수+1 별 오일러 피 함수 적용
        divisor_list: list[int] = []
        factorization_dict = factorization_pollard_rho(N)
        for index, (i, j) in enumerate(factorization_dict.items()):
            if index == 0:
                for k in range(j + 1):
                    divisor_list.append(i**k)
            else:
                divisor_list_sub = []
                for d in divisor_list:
                    for k in range(j + 1):
                        divisor_list_sub.append(d * i**k)
                divisor_list += divisor_list_sub
        divisor_list = list(set(divisor_list))
        print(sum([euler_phi(i + 1) for i in divisor_list]))