# 1644 소수의 연속합

from bisect import bisect_left

finder_limit = 4000000
prime_list: list[bool] = [True for i in range(0, finder_limit + 1)]
prime_list[0] = False
prime_list[1] = False
for x in range(1, int(finder_limit**0.5) + 1):
    if prime_list[x]:
        prime_list[x : finder_limit + 1 : x] = [False] * (finder_limit // x)
        prime_list[x] = True
    else:
        continue
prime_list2:list[int] = [i for i, j in enumerate(prime_list) if j]
accumulated_sum_prime_list = [0]

for i, j in enumerate(prime_list2):
    accumulated_sum_prime_list.append(j+accumulated_sum_prime_list[-1])

N = int(input())
answer = 0
prime_list_length = len(prime_list2)
for i,j in enumerate(accumulated_sum_prime_list):
    if j < N:
        continue
    elif i != 0 and j - accumulated_sum_prime_list[i-1] > N:
        break
    else:
        pointer_to_cut = bisect_left(accumulated_sum_prime_list, j-N)
        if j-N==accumulated_sum_prime_list[pointer_to_cut]:
            answer += 1
print(answer)