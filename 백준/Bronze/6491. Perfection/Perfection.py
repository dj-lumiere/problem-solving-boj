# 6491 Perfection


def is_perfect(target):
    target_divisors = []

    for i in range(1, int(target**0.5) + 1):
        if target % i:
            continue
        target_divisors.extend([i, target // i])

    target_divisor_sum = sum(set(target_divisors)) - target
    if target_divisor_sum == target:
        return f"{target} PERFECT"
    if target_divisor_sum > target:
        return f"{target} ABUNDANT"
    if target_divisor_sum < target:
        return f"{target} DEFICIENT"


number_list = []
while True:
    try:
        number_list_sub = input().split(" ")
        number_list_sub = [int(i) for i in number_list_sub if i]
        number_list.extend(number_list_sub)
    except:
        break
number_list.pop()
number_list = list(map(is_perfect, number_list))
print(*number_list, sep="\n")