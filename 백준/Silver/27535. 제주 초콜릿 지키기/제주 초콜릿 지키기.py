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
        H, T, C, K, G = (int(input()) for _ in range(5))
        M = int(input())
        previous_total = H + T + C + K + G
        for _ in range(M):
            h, t_, c, k, g = (int(input()) for _ in range(5))
            H -= h
            T -= t_
            C -= c
            K -= k
            G -= g
            current_total = H + T + C + K + G
            base = previous_total % 10 if previous_total % 10 > 1 else 10
            if current_total == 0:
                converted = '0'
            else:
                digits = ''
                temp = current_total
                while temp > 0:
                    digits = str(temp % base) + digits
                    temp = temp // base
                converted = digits
            answer = f"{converted}7H"
            answers.append(f"{answer}")
            if current_total == 0:
                second_line = "NULL"
            else:
                types = [('C', C), ('G', G), ('H', H), ('K', K), ('T', T)]
                sorted_types = sorted(types, key=lambda x: (-x[1], x[0]))
                second_line = ''.join([x[0] for x in sorted_types if x[1] > 0]) or "NULL"
            answer = second_line
            answers.append(f"{answer}")
            previous_total = current_total
    print(*answers, sep="\n")