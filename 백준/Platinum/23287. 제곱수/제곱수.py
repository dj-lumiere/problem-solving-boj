# 17646 제곱수의 합 2 (More Huge)

from math import gcd
from random import randint
from sys import setrecursionlimit
from collections import Counter
from decimal import Decimal

setrecursionlimit(200000)

N: int = int(input())
prime_list: list[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]


def is_prime(n: int) -> bool:
    # prime list의 원소를 미리 소수로 처리
    if n in prime_list:
        return True
    # 짝수는 소수가 아님
    if n == 1 or n % 2 == 0:
        return False
    # (n-1) = 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
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


def factorize_big(n: int) -> list[int]:
    factors: list[int] = []
    next_N: int = n
    for i in prime_list:
        while next_N % i == 0:
            factors.append(i)
            next_N //= i
    while next_N > 1:
        factor = pollard_rho(next_N)
        factors.append(factor)
        next_N //= factor
    return factors


def how_many_squares(n: int) -> int:
    factor_dict: dict[int, int] = Counter(factorize_big(n))
    # 4**n * (8k+7) 형태의 숫자면 최소 4개 필요
    if (n >> ((factor_dict[2] >> 1) << 1)) % 8 == 7:
        return 4
    # 제곱수면 1개면 충분
    elif int(n**0.5) ** 2 == n:
        return 1
    else:
        for (i, j) in factor_dict.items():
            # (4k+3)**(2l+1) 형태의 인수가 존재하면 3개
            if i % 4 == 3 and j % 2 == 1:
                return 3
        # 아니면 2개
        return 2


def cornacchia(p: int) -> tuple[int, int]:
    # x^2+y^2=p 풀기
    a: int = tonelli_shanks(p)
    b: int = p
    while a**2 > p:
        b %= a
        if b**2 < p:
            return (b, int(Decimal(p - b**2).sqrt()))
        a %= b
    return (a, int(Decimal(p - a**2).sqrt()))


def tonelli_shanks(p: int) -> int:
    # x^2=-1(mod p)인 p가 존재한다 가정
    # p-1을 2**S*Q(Q는 홀수, S는 0 이상)으로 나누기
    q: int = p - 1
    s: int = 0
    while not q % 2:
        q >>= 1
        s += 1
    # 이차 잉여군이 아닌 z를 찾기
    z: int = randint(2, p - 1)
    while pow(z, (p - 1) >> 1, p) == 1:
        z = randint(2, p - 1)
    # 초깃값 세팅
    m: int = s
    c: int = pow(z, q, p)
    t: int = pow(p - 1, q, p)
    r: int = pow(p - 1, (q + 1) >> 1, p)
    if t == 0:
        return 0
    while t != 0 and t != 1:
        t_next: int = t
        i = 0
        while t_next % p != 1:
            # t**(2**i)인 0<i<m 찾기
            t_next = pow(t_next, 2, p)
            i += 1
        b: int = pow(c, pow(2, m - i - 1, p), p)
        m = i
        c = pow(b, 2, p)
        t = (t * c) % p
        r = (r * b) % p
    return r


def get_2_squares(n: int) -> tuple[int, int]:
    # 인수들을 받아봄
    a, b = 1, 0
    multiplier: int = 1
    factor_dict: dict[int, int] = Counter(factorize_big(n))
    new_n: int = 1
    for (i, j) in factor_dict.items():
        # 인수가 2개 이상일 경우 단체로 곱해 multiplier로 빼두기
        multiplier *= pow(i, (j >> 1))
        new_n *= pow(i, j % 2)
        factor_dict[i] -= (j >> 1) << 1
    for (i, j) in factor_dict.items():
        if i == 2 and j % 2:
            # 2가 홀수개면 1,1로 변형하기
            a, b = 1, 1
        elif i % 4 == 1 and j:
            # 4k+1 형 인수면 Cornacchia 알고리즘 쓰기
            x, y = cornacchia(i)
            if a == 1 and b == 0:
                a, b = x, y
            else:
                a, b = abs(a * x - b * y), b * x + a * y
    return (a * multiplier, b * multiplier)


def get_3_squares(n: int):
    # 인수들을 받아봄
    factor_dict: dict[int, int] = Counter(factorize_big(n))
    a, b, c = 0, 0, 0
    multiplier: int = 1
    new_n: int = 1
    for (i, j) in factor_dict.items():
        # 인수가 2개 이상일 경우 단체로 곱해 multiplier로 빼두기
        multiplier *= pow(i, (j >> 1))
        new_n *= pow(i, j % 2)
    # Brute Force Method로 두 개의 제곱수로 될 때까지 시도하기
    t: int = 1
    while how_many_squares(new_n - t**2) != 2:
        t += 1
    a, b, c = *get_2_squares(new_n - t**2), t
    return (a * multiplier, b * multiplier, c * multiplier)


def get_4_squares(n: int):
    # 인수들을 받아봄
    factor_dict: dict[int, int] = Counter(factorize_big(n))
    multiplier: int = 1
    new_n: int = n
    a: int = 1
    # 4**k*(8n+7(i.e. new_n)) 형태로 바꾸기
    if 2 in factor_dict:
        multiplier <<= factor_dict[2] >> 1
        new_n >>= (factor_dict[2] >> 1) << 1
        factor_dict[2] = factor_dict[2] % 2
    # new_n - 1은 3개로 쪼개질 수 있음.
    b, c, d = get_3_squares(new_n - 1)
    return (a * multiplier, b * multiplier, c * multiplier, d * multiplier)


number_of_squares = how_many_squares(N)
if number_of_squares == 1:
    print(0, 0, 0, int(Decimal(N).sqrt()))
elif number_of_squares == 2:
    print(0, 0, *get_2_squares(N))
elif number_of_squares == 3:
    print(0, *get_3_squares(N))
else:
    print(*get_4_squares(N))