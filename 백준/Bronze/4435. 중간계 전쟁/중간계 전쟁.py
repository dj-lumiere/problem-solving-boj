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
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        gandalf = list(map(int, [input() for _ in range(6)]))
        sauron = list(map(int, [input() for _ in range(7)]))
        gandalf_score = gandalf[0] * 1 + gandalf[1] * 2 + gandalf[2] * 3 + gandalf[3] * 3 + gandalf[4] * 4 + gandalf[
            5] * 10
        sauron_score = sauron[0] * 1 + sauron[1] * 2 + sauron[2] * 2 + sauron[3] * 2 + sauron[4] * 3 + sauron[5] * 5 + \
                       sauron[6] * 10
        if gandalf_score > sauron_score:
            answer = f"Battle {hh}: Good triumphs over Evil"
        elif gandalf_score < sauron_score:
            answer = f"Battle {hh}: Evil eradicates all trace of Good"
        else:
            answer = f"Battle {hh}: No victor on this battle field"
        answers.append(f"{answer}")
    print(*answers, sep="\n")