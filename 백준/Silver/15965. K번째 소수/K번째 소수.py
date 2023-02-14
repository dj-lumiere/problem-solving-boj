# 15965 K번째 소수

# 50만번째 소수가 7,368,787이므로, 800만을 기준으로 잡고 에라토스테네스의 체로 소수 탐색
finder_limit = 8000000
prime_list: list[bool] = [True for i in range(0, finder_limit + 1)]
prime_list[0] = False
prime_list[1] = False
for x in range(1, int(finder_limit**0.5) + 1):
    if prime_list[x]:
        prime_list[x : finder_limit + 1 : x] = [False] * (finder_limit // x)
        prime_list[x] = True
prime_list2 = [i for i, j in enumerate(prime_list) if j]
print(prime_list2[int(input())-1])