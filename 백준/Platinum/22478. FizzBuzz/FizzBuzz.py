# 22478 FizzBuzz

from math import floor, log10


def digit_length(number: int) -> int:
    return floor(log10(number)) + 1


def find_fizzbuzz_string_length(upper_bound: int) -> int:
    if upper_bound == 0:
        return 0
    upper_bound_digit: int = digit_length(upper_bound)
    fizzbuzz_string_length: list[int] = [0 for i in range(upper_bound_digit + 1)]
    for i, v in enumerate(fizzbuzz_string_length):
        if i == 0:
            continue
        number_lower_limit: int = 10 ** (i - 1)
        number_upper_limit: int = min(upper_bound, 10**i - 1)
        fizzbuzz_string_length[i] += (number_upper_limit - number_lower_limit + 1) * i
        fizz_only_count: int = number_upper_limit // 3 - (number_lower_limit - 1) // 3
        buzz_only_count: int = number_upper_limit // 5 - (number_lower_limit - 1) // 5
        fizzbuzz_only_count: int = (
            number_upper_limit // 15 - (number_lower_limit - 1) // 15
        )
        fizz_only_count -= fizzbuzz_only_count
        buzz_only_count -= fizzbuzz_only_count
        fizzbuzz_string_length[i] -= (
            fizz_only_count + buzz_only_count + fizzbuzz_only_count
        ) * i
        fizzbuzz_string_length[i] += (
            fizz_only_count + buzz_only_count + fizzbuzz_only_count * 2
        ) * 4
    return sum(fizzbuzz_string_length)


def find_minimal_number(length: int) -> tuple[int, int]:
    lower_bound = 0
    upper_bound = length + 1
    while lower_bound + 1 < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        fizzbuzz_string_length_until_mid = find_fizzbuzz_string_length(mid)
        if fizzbuzz_string_length_until_mid > length:
            upper_bound = mid
        elif fizzbuzz_string_length_until_mid <= length:
            lower_bound = mid
    return (lower_bound, length - find_fizzbuzz_string_length(lower_bound))


def find_string(position):
    lower_limit_for_contain, leftover = find_minimal_number(position - 1)
    answer = ""
    next_number = lower_limit_for_contain + 1
    next_length = 20
    while next_length > 0:
        number_to_string = ""
        if not next_number % 15:
            number_to_string = "FizzBuzz"
        elif not next_number % 5:
            number_to_string = "Buzz"
        elif not next_number % 3:
            number_to_string = "Fizz"
        else:
            number_to_string = str(next_number)
        answer += number_to_string[leftover:]
        next_length -= len(number_to_string) - leftover
        next_number += 1
        leftover = 0
    return answer[:20]


N = int(input())
print(find_string(N))