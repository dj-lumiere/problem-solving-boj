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
    t = INF
    answers = []
    for hh in range(t):
        s = input()
        if s == '0':
            break
        n = int(s)
        if s == s[::-1]:
            answer = 0
        else:
            l = len(s)
            half = (l + 1) // 2
            first_half = s[:half]
            if l % 2 == 0:
                mirrored = first_half + first_half[::-1]
            else:
                mirrored = first_half + first_half[:-1][::-1]
            if mirrored >= s:
                candidate = int(mirrored)
            else:
                first_half_inc = str(int(first_half) + 1).zfill(half)
                if len(first_half_inc) > half:
                    candidate = int('1' + '0' * (l - 1) + '1')
                else:
                    if l % 2 == 0:
                        mirrored = first_half_inc + first_half_inc[::-1]
                    else:
                        mirrored = first_half_inc + first_half_inc[:-1][::-1]
                    candidate = int(mirrored)
            answer = candidate - n
        answers.append(f"{answer}")
    print(*answers, sep="\n")