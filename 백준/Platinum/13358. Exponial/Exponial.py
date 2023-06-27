# 13358 Exponial
from random import randint


# a까지의 소수를 찾기
def find_prime(a: int) -> list[int]:
    if a == 1:
        return []
    else:
        finder_limit = a
        prime_list: list[int] = [1 for i in range(0, finder_limit + 1)]
        prime_list[0] = 0
        prime_list[1] = 0
        for x in range(1, int(finder_limit**0.5) + 1):
            if prime_list[x]:
                prime_list[x : finder_limit + 1 : x] = [0] * (finder_limit // x)
                prime_list[x] = 1
            else:
                continue
        return [i for i, v in enumerate(prime_list) if v]


prime_list = find_prime(int(10**4.5) + 1)


def euler_phi(M: int):
    factor_list = []
    result = M
    next_M = M
    for i in prime_list:
        if i * i > M:
            break
        if M % i == 0:
            factor_list.append(i)
            next_M //= i
            while next_M % i == 0:
                next_M //= i
    for i in factor_list:
        result = result * (i - 1) // i
    if next_M != 1 and next_M not in factor_list:
        result = result * (next_M - 1) // next_M
    return result


def sol(N, M):
    if N % M == 0:
        return 0
    if M == 1:
        return 0
    if N == 1:
        return 1 % M
    elif N == 2:
        return 2 % M
    elif N == 3:
        return 9 % M
    elif N == 4:
        return pow(4, 9, M)
    return pow(N, sol(N - 1, euler_phi(M)) + euler_phi(M), M)


N, M = map(int, input().split(" "))
print(sol(N, M) % M)