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
        n = int(input())
        files = []
        for _ in range(n):
            seq = []
            while True:
                num = int(input())
                if num == -1:
                    break
                seq.append(num)
            files.append(seq)
        K = 1
        while True:
            seen = set()
            unique = True
            for f_seq in files:
                prefix = tuple(f_seq[:K]) if len(f_seq) >= K else tuple(f_seq + [0] * (K - len(f_seq)))
                if prefix in seen:
                    unique = False
                    break
                seen.add(prefix)
            if unique:
                answer = K
                break
            else:
                K += 1
        answers.append(f"{answer}")
    print(*answers, sep="\n")