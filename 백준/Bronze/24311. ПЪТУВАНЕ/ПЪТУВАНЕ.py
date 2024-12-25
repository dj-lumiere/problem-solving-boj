from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        t1 = int(input())
        t2 = int(input())
        t3 = int(input())
        t4 = int(input())
        t5 = int(input())
        br = int(input())
        t6 = int(input())
        conference_time = t1 * 60 + t2
        required_arrival = conference_time - 10
        hotel_time = t6 * (br + 1)
        required_before = t3 + hotel_time
        latest_arrival = required_arrival - required_before
        travel_time = t4 * 60 + t5
        departure_time = latest_arrival - travel_time
        hour = departure_time // 60
        minute = departure_time % 60
        answer = f"{hour:02} {minute:02}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")