# 11690 LCM(1, 2, ..., n)
from math import ceil


N = int(input())
finder_limit = ceil(N**0.5)
finder_limit2 = ceil(N**0.25)
prime_list = [False] * 2 + [True for i in range(2, finder_limit + 1)]
for x in range(2, finder_limit2 + 1):
    if prime_list[x]:
        prime_list[x::x] = [False] * (finder_limit // x)
        prime_list[x] = True

prime_list2 = [i for i, j in enumerate(prime_list) if j]
prime_list3 = []
for i in range(1, ceil(N / finder_limit)):
    prime_list: list[bool] = [True for _ in range(finder_limit)]
    for x in prime_list2:
        starting_point = ceil(i * finder_limit / x) * x - i * finder_limit
        prime_list[starting_point::x] = [False] * (
            ((i + 1) * finder_limit - 1) // x - (i * finder_limit - 1) // x
        )
    prime_list3 += [
        j + finder_limit * i
        for j, k in enumerate(prime_list)
        if k and (j + finder_limit * i <= N)
    ]

mod = 1
for i in prime_list2:
    next_i = i
    while next_i <= N:
        mod = (mod * i) & 0xffffffff
        next_i *= i
for i in prime_list3:
    mod = (mod * i) & 0xffffffff

print(mod)
