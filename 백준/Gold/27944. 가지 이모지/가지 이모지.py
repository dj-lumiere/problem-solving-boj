# 27944 가지 이모지
# 답은 반드시 ai의 약수이거나 ai+1의 약수
# 전부 1씩더하고 제일 작은수의 약수로 나눈 나머지가 1초과면 바로컷

from math import gcd

# a까지의 소수를 찾기
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
            else:
                continue
        return [i for (i, j) in enumerate(prime_list) if j]


prime_list = find_prime(10**6)

N = int(input())
A = list(map(int, input().split(" ")))
prime_factors1 = [i for i in prime_list if A[0] % i == 0]
prime_factors2 = [i for i in prime_list if (A[0] + 1) % i == 0]
prime_checklist = list(set(prime_factors1 + prime_factors2))
is_answer = True
answer = 1

for i in prime_checklist:
    pattern = [A[i] for i in range(N)]
    is_answer = True
    for (j, k) in enumerate(A):
        if k % i == 0:
            continue
        elif (k + 1) % i == 0:
            pattern[j] += 1
        else:
            is_answer = False
            break
    if not is_answer:
        continue
    else:
        answer = max(answer, gcd(*pattern))
print(answer)