# 19577 수학은 재밌어


def find_prime(a: int) -> list[int]:
    if a == 1:
        return []
    finder_limit = a
    prime_list: list[int] = [1 for i in range(0, finder_limit + 1)]
    prime_list[0] = 0
    prime_list[1] = 0
    for x in range(1, int(finder_limit**0.5) + 1):
        if not prime_list[x]:
            continue
        prime_list[x : finder_limit + 1 : x] = [0] * (finder_limit // x)
        prime_list[x] = 1
    return [i for i, v in enumerate(prime_list) if v]


prime_list = find_prime(int(10**4.5) + 1)


def euler_phi(N):
    result = N
    for v in prime_list:
        if v > N:
            break
        if N % v:
            continue
        result *= v - 1
        result //= v
    return result


def sol(N):
    if N == 1:
        return 1
    result_candidate = []
    for i in range(1, int(N**0.5) + 1):
        if not N % i and euler_phi(i) == N // i:
            result_candidate.append(i)
        if not N % i and euler_phi(N // i) == i:
            result_candidate.append(N // i)
    if not result_candidate:
        return -1
    return min(result_candidate)


# n//x=phi(x)
N = int(input())
print(sol(N))