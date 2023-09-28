# 1792 공약수

from sys import stdin


def input():
    return stdin.readline().strip()


def calculate_mobius_function(limit):
    result = [1] * (limit + 1)
    check = [False] * (limit + 1)
    result[1] = 1
    check[1] = True
    for i in range(2, limit + 1):
        if check[i]:
            continue
        j = 1
        while i * j <= limit:
            check[i * j] = True
            result[i * j] = (result[i * j] * -1) if j % i else 0
            j += 1
    return result


def calculate_pairs(a, b, d, mobius_prefix_sum):
    a //= d
    b //= d
    result = 0
    possible_changes = []
    for i in range(1, int(a**0.5) + 1):
        if i == a // i:
            possible_changes.append(i)
        else:
            possible_changes.extend([i, a // i])
    for i in range(1, int(b**0.5) + 1):
        if i == b // i:
            possible_changes.append(i)
        else:
            possible_changes.extend([i, b // i])
    possible_changes = sorted(list(set(possible_changes)))
    pair_count_sub = [(a // i) * (b // i) for i in possible_changes]
    result = 0
    previous_value = 0
    for i, (v1, v2) in enumerate(zip(possible_changes, pair_count_sub)):
        if i == 0:
            result += (mobius_prefix_sum[v1]) * v2
            previous_value = v1
            continue
        result += (mobius_prefix_sum[v1] - mobius_prefix_sum[previous_value]) * v2
        previous_value = v1
    return result


mobius_value = calculate_mobius_function(50000)
mobius_prefix_sum = [0] * 50001
for i in range(1, 50001):
    mobius_prefix_sum[i] = mobius_value[i] + mobius_prefix_sum[i - 1]
T = int(input())
for _ in range(T):
    a, b, d = map(int, input().split(" "))
    print(calculate_pairs(a, b, d, mobius_prefix_sum))