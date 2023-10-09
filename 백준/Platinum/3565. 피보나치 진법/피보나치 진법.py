# 3565 피보나치 진법

from bisect import bisect_right

fib = [0, 1, 1]
fib_sum = [0, 1, 2]

for _ in range(65):
    fib.append(sum(fib[-2:]))
    fib_sum.append(fib[-1] + fib_sum[-1])

digit_count = []
for i in range(65):
    if i == 0:
        digit_count.append(0)
        continue
    digit_count.append(i * fib[i])

accumulated_digit_count = []
for i in range(65):
    if i == 0:
        accumulated_digit_count.append(0)
        continue
    accumulated_digit_count.append(accumulated_digit_count[-1] + digit_count[i])

one_count = [0, 1, 1]
for i in range(3, 65):
    one_count.append(fib[i] + sum(one_count[: i - 1]))

accumulated_one_count = []
for i in range(65):
    if i == 0:
        accumulated_one_count.append(0)
        continue
    accumulated_one_count.append(accumulated_one_count[-1] + one_count[i])

#print(fib)
#print(fib_sum)
#print(digit_count)
#print(accumulated_digit_count)
#print(one_count)
#print(accumulated_one_count)

def find_zeckendorf_form(N: int):
    result = []
    next_n = N
    for i, v in enumerate(reversed(fib)):
        if i + 2 >= len(fib):
            break
        if N < v:
            continue
        if next_n >= v:
            next_n -= v
            result.append(1)
        else:
            result.append(0)
    return result


def find_one_count_until_N(N: int):
    if N <= 0:
        return 0
    lastly_full_counted_digit = bisect_right(fib_sum, N)
    if N != fib_sum[lastly_full_counted_digit]:
        lastly_full_counted_digit -= 1
    full_counted_digit_count = fib_sum[lastly_full_counted_digit]
    leftover_number_count = N - full_counted_digit_count
    #print(N, lastly_full_counted_digit,full_counted_digit_count,leftover_number_count)
    return accumulated_one_count[lastly_full_counted_digit] + leftover_number_count + find_one_count_until_N(leftover_number_count - 1)


def find_one_count(N: int):
    if N == 0:
        return 0
    lastly_full_counted_digit = bisect_right(accumulated_digit_count, N)
    if N != accumulated_digit_count[lastly_full_counted_digit]:
        lastly_full_counted_digit -= 1
    full_counted_digit_count = accumulated_digit_count[lastly_full_counted_digit]
    leftover_number_count = N - full_counted_digit_count
    full_number_count, leftover_digit_count = divmod(
        leftover_number_count, lastly_full_counted_digit + 1
    )
    max_number = (
        fib_sum[lastly_full_counted_digit]
        + full_number_count
        + (1 if leftover_digit_count else 0)
    )
    #print(N, lastly_full_counted_digit,full_counted_digit_count,leftover_number_count,full_number_count,leftover_digit_count,max_number)
    return (
        accumulated_one_count[lastly_full_counted_digit]
        + full_number_count
        + find_one_count_until_N(full_number_count - 1)
        + sum(
            v
            for i, v in enumerate(find_zeckendorf_form(max_number))
            if i < leftover_digit_count
        )
    )

n = int(input())
#print(find_one_count_until_N(n))
print(find_one_count(n))