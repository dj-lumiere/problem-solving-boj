# 5768 Divide and Conquer


def divisor_count(target):
    target_divisors = []

    for i in range(1, int(target**0.5) + 1):
        if target % i:
            continue
        target_divisors.extend([i, target // i])

    target_divisors = list(set(target_divisors))
    return len(target_divisors)


while True:
    a, b = map(int, input().split(" "))
    result = []
    if not any((a, b)):
        break
    for i in range(a, b + 1):
        i_divisor_count = divisor_count(i)
        result.append((i, i_divisor_count))
    result.sort(key=lambda x: (-x[1], -x[0]))
    print(*result[0])