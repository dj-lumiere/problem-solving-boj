# 4355
# 소인수분해
# 오일러 피 함수 적용
finder_limit = 31623
prime_list: list[bool] = [False]*2+[True for i in range(0, finder_limit + 1)]
for x in range(1, int(finder_limit**0.5) + 1):
    if prime_list[x]:
        prime_list[x : finder_limit + 1 : x] = [False] * (finder_limit // x)
        prime_list[x] = True
prime_list2 = [i for i, j in enumerate(prime_list) if j]
while True:
    N = int(input())
    if N == 0:
        break
    elif N == 1:
        print(0)
    else:
        # 소인수 분해 후
        coprime_count = N
        next_factor = N
        for j in prime_list2:
            if next_factor % j == 0 and j ** 2 <= N:
                coprime_count //= j
                coprime_count *= (j-1)
            while next_factor % j == 0 and j ** 2 <= N:
                next_factor = next_factor // j
        if next_factor != 1:
            coprime_count //= next_factor
            coprime_count *= (next_factor - 1)
        print(coprime_count)