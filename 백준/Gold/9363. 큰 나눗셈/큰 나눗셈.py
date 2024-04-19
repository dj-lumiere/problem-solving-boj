from collections import defaultdict

# 9363 큰 나눗셈


finder_limit = 10 ** 3
prime_list: list[bool] = [True for i in range(0, finder_limit + 1)]
prime_list[0] = False
prime_list[1] = False
for x in range(1, int(finder_limit ** 0.5) + 1):
    if prime_list[x]:
        prime_list[x: finder_limit + 1: x] = [False] * (finder_limit // x)
        prime_list[x] = True
prime_list2 = [i for i, j in enumerate(prime_list) if j]

T = int(input())

for i in range(1, T + 1):
    A, B = list(map(int, input().split(" ")))
    a_list = list(map(int, input().split(" ")))
    b_list = list(map(int, input().split(" ")))
    factorization = defaultdict(int)
    for x in prime_list2:
        factorization[x] = 0
    for a in a_list:
        next_factor = a
        for j in prime_list2:
            while next_factor % j == 0:
                factorization[j] += 1
                next_factor = next_factor // j
        if next_factor > 1000:
            factorization[next_factor] += 1
    for b in b_list:
        next_factor = b
        for j in prime_list2:
            while next_factor % j == 0:
                factorization[j] -= 1
                next_factor = next_factor // j
        if next_factor > 1000:
            factorization[next_factor] -= 1
    numerator = 1
    denominator = 1
    for p, q in factorization.items():
        if q < 0:
            denominator *= p ** (-1 * q)
        elif q > 0:
            numerator *= p ** q
    print(f"Case #{i}: {numerator} / {denominator}")