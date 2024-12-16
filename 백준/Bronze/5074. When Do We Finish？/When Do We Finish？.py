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
    for _ in range(t):
        s_time, d_time = input(), input()
        if s_time == "00:00" and d_time == "00:00":
            break
        sh, sm = map(int, s_time.split(':'))
        dh, dm = map(int, d_time.split(':'))
        start_total = sh * 60 + sm
        duration_total = dh * 60 + dm
        end_total = start_total + duration_total
        days = end_total // (24 * 60)
        rem = end_total % (24 * 60)
        eh = rem // 60
        em = rem % 60
        if days > 0:
            answer = f"{eh:02d}:{em:02d} +{days}"
        else:
            answer = f"{eh:02d}:{em:02d}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")