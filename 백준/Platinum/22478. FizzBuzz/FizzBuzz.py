# 22478 FizzBuzz

from math import floor, log10


def digit_length(number: int) -> int:
    return floor(log10(number)) + 1


def find_fizzbuzz_string_length(upper_bound: int) -> int:
    if upper_bound == 0:
        return 0
    upper_bound_digit: int = digit_length(upper_bound)
    fizzbuzz_string_length: list[int] = [0 for i in range(upper_bound_digit + 1)]
    for i, _ in enumerate(fizzbuzz_string_length):
        if i == 0:
            continue
        lower_limit: int = 10 ** (i - 1)
        upper_limit: int = min(upper_bound, 10**i - 1)
        fizzbuzz_string_length[i] += (upper_limit - lower_limit + 1) * i
        fizzbuzz_count: int = upper_limit // 15 - (lower_limit - 1) // 15
        fizz_count: int = upper_limit // 3 - (lower_limit - 1) // 3 - fizzbuzz_count
        buzz_count: int = upper_limit // 5 - (lower_limit - 1) // 5 - fizzbuzz_count
        fizzbuzz_string_length[i] -= (fizz_count + buzz_count + fizzbuzz_count) * i
        fizzbuzz_string_length[i] += (fizz_count + buzz_count + fizzbuzz_count * 2) * 4
    return sum(fizzbuzz_string_length)


def find_minimal_number(length: int) -> tuple[int, int]:
    lower_bound: int = 0
    upper_bound: int = length + 1
    while lower_bound + 1 < upper_bound:
        mid: int = (lower_bound + upper_bound) // 2
        fizzbuzz_string_length_until_mid: int = find_fizzbuzz_string_length(mid)
        if fizzbuzz_string_length_until_mid > length:
            upper_bound = mid
        elif fizzbuzz_string_length_until_mid <= length:
            lower_bound = mid
    return (lower_bound, length - find_fizzbuzz_string_length(lower_bound))


def find_string(position):
    lower_limit_for_contain, leftover = find_minimal_number(position - 1)
    answer: str = ""
    next_number: int = lower_limit_for_contain + 1
    next_length: int = 20
    while next_length > 0:
        next_str: str = ""
        if not next_number % 15:
            next_str = "FizzBuzz"
        elif not next_number % 5:
            next_str = "Buzz"
        elif not next_number % 3:
            next_str = "Fizz"
        else:
            next_str = str(next_number)
        answer += next_str[leftover:]
        next_length -= len(next_str) - leftover
        next_number += 1
        leftover = 0
    return answer[:20]


N = int(input())
print(find_string(N))