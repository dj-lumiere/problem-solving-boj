# 29728 실버와 소수는 둘다 S로 시작한다


def get_prime_sieve(limit: int) -> list[bool]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit**0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2 : limit + 1 : i] = [False] * (limit // i - 1)
    return is_prime


LIMIT = 5000000
prime_check = get_prime_sieve(LIMIT + 1)
answer = [[0, 0] for _ in range(LIMIT + 1)]
for i in range(1, LIMIT + 1):
    if i == 1:
        answer[i] = [1, 0]
    elif not prime_check[i]:
        answer[i][0] = answer[i - 1][0] + 1
        answer[i][1] = answer[i - 1][1]
    elif prime_check[i] and not prime_check[i - 1]:
        answer[i][0] = answer[i - 1][0] - 1
        answer[i][1] = answer[i - 1][1] + 2
    else:
        answer[i][0] = answer[i - 1][0]
        answer[i][1] = answer[i - 1][1] + 1

N = int(input())
print(*answer[N])