# 6975 Deficient, Perfect, and Abundant


def is_perfect(target):
    target_divisors = []

    for i in range(1, int(target**0.5) + 1):
        if target % i:
            continue
        target_divisors.extend([i, target // i])

    target_divisor_sum = sum(set(target_divisors)) - target
    if target_divisor_sum == target:
        return f"{target} is a perfect number."
    if target_divisor_sum > target:
        return f"{target} is an abundant number."
    if target_divisor_sum < target:
        return f"{target} is a deficient number."

N = int(input())
number_list = [int(input()) for _ in range(N)]
number_list = list(map(is_perfect, number_list))
print(*number_list, sep="\n\n")