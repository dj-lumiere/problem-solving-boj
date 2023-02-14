# 4233 가짜소수

from math import log2


def find_prime(a: int) -> list[int]:
    if a == 1:
        return []
    else:
        finder_limit = a
        prime_list: list[bool] = [True for i in range(0, finder_limit + 1)]
        prime_list[0] = False
        prime_list[1] = False
        for x in range(1, int(finder_limit**0.5) + 1):
            if prime_list[x]:
                prime_list[x : finder_limit + 1 : x] = [False] * (finder_limit // x)
                prime_list[x] = True
        prime_list2 = [i for i, j in enumerate(prime_list) if j]
        return prime_list2


prime_list = find_prime(10**5)

while True:
    p, a = list(map(int, input().split(" ")))
    if p == a == 0:
        break
    else:
        if p < a:
            p, a = a, p
        # p가 소수인지 아닌지 확정짓기
        p_prime_check = True
        for i in prime_list:
            if i * i > p:
                break
            elif not p % i:
                p_prime_check = False
                break
        if p_prime_check:
            print("no")
        else:
            # a**p%p 구하기
            digits = int(log2(p)) + 1
            a_power_list = [0 for i in range(digits)]
            p_binary_list = [p // (2**i) % 2 for i in range(digits)]
            a_power_list[0] = a
            result = 1
            for i in range(1, digits):
                a_power_list[i] = a_power_list[i - 1] ** 2 % p
            for i, j in zip(a_power_list, p_binary_list):
                if j:
                    result = result * i % p
            if result == a:
                print("yes")
            else:
                print("no")