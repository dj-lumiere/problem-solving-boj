# 11439 이항 계수 5


def find_prime() -> list[bool]:
    a = 4000000
    prime_list: list[bool] = [True for i in range(0, a + 1)]
    prime_list[0] = False
    prime_list[1] = False
    prime_list2 = []
    for x in range(1, a + 1):
        if prime_list[x]:
            prime_list[x : a + 1 : x] = [False] * (a // x)
            prime_list[x] = True
            prime_list2.append(x)
        else:
            continue
    return prime_list2


prime_list = find_prime()

prime_length = len(prime_list)

factor_counter_up = [0 for i in range(prime_length)]
factor_counter_down = [0 for i in range(prime_length)]

N, K, M = list(map(int, input().split(" ")))

if K * 2 > N:
    K = N - K
for i, j in enumerate(prime_list):
    if j > N:
        break
    next_factor = 1
    while next_factor <= N:
        next_factor *= j
        factor_counter_up[i] += N // next_factor - (N - K) // next_factor
        factor_counter_down[i] += K // next_factor
factor_counter = [i - j for i, j in zip(factor_counter_up, factor_counter_down)]
remainder = 1
for i, j in zip(prime_list, factor_counter):
    if i > N:
        break
    if j == 0:
        continue
    else:
        remainder = remainder * (i**j) % M
print(remainder)
