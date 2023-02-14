# 11690 LCM(1, 2, ..., n)

N = int(input())
prime_list: list[bool] = [False] * 2 + [True for i in range(2, 10000 + 1)]
for x in range(2, 100 + 1):
    if prime_list[x]:
        prime_list[x::x] = [False] * (10000 // x)
        prime_list[x] = True

prime_list2 = [i for i, j in enumerate(prime_list) if j]
prime_list3 = []
for i in range(1, 10000):
    prime_list: list[bool] = [True for i in range(10000)]
    for x in prime_list2:
        starting_point = (x - (i * 10000)) % x
        prime_list[starting_point::x] = [False] * (
            ((i + 1) * 10000 - 1) // x - (i * 10000 - 1) // x
        )
    prime_list3 += [j + 10000 * i for j, k in enumerate(prime_list) if k]

mod = 1
for i in prime_list2:
    if i <= N:
        next_i = i
        while next_i <= N:
            mod = mod * i % 4294967296
            next_i *= i
for i in prime_list3:
    if i <= N:
        mod = mod * i % 4294967296

print(mod)