from decimal import getcontext
from sys import stderr, stdout

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
        rh = int(input())
        rv = int(input())
        sh = int(input())
        sv = int(input())
        n = int(input())
        min_price = INF
        for _ in range(n):
            mrh = int(input())
            mrv = int(input())
            msh = int(input())
            msv = int(input())
            price = int(input())
            for rot in range(2):
                current_rh = mrh
                current_rv = mrv
                current_sh = msh
                current_sv = msv
                if rot == 1:
                    current_rh, current_rv = current_rv, current_rh
                    current_sh, current_sv = current_sv, current_sh
                h_mon1 = (rh + current_rh - 1) // current_rh
                v_mon1 = (rv + current_rv - 1) // current_rv
                h_mon2 = (sh + current_sh - 1) // current_sh
                v_mon2 = (sv + current_sv - 1) // current_sv
                h_mon = max(h_mon1, h_mon2)
                v_mon = max(v_mon1, v_mon2)
                total_price = h_mon * v_mon * price
                if total_price < min_price:
                    min_price = total_price
        answer = min_price
        answers.append(f"{answer}")
    print(*answers, sep="\n")