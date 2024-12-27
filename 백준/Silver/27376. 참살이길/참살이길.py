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
        n, k = (int(input()) for _ in range(2))
        traffic_lights = [tuple(int(input()) for _ in range(3)) for _ in range(k)]
        traffic_lights.sort()
        total_delay = 0
        for x_i, t_i, s_i in traffic_lights:
            arrival_time = x_i + total_delay
            if arrival_time < s_i:
                wait_time = s_i - arrival_time
            else:
                cycle_time = arrival_time - s_i
                cycle_pos = cycle_time % (2 * t_i)
                if cycle_pos < t_i:
                    wait_time = 0
                else:
                    wait_time = 2 * t_i - cycle_pos
            total_delay += wait_time
        total_time = n + total_delay
        answer = total_time
        answers.append(f"{answer}")
    print(*answers, sep="\n")