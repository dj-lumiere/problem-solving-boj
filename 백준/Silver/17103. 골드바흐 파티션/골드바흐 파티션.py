# 17103 골드바흐 파티션

from bisect import bisect_left


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
        return [i for i, v in enumerate(prime_list) if v]


prime_list = find_prime(1000000)


def goldbach_partition_count(target: int) -> int:
    answer = 0
    for i, v in enumerate(prime_list):
        if target - v > v:
            continue
        if target - 2 < v:
            break
        other_pointer = bisect_left(prime_list, target - v)
        if prime_list[other_pointer] == target - v:
            answer += 1
    return answer


T = int(input())
for _ in range(T):
    test = int(input())
    print(goldbach_partition_count(test))