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
        n, a, b = int(input()), int(input()), int(input())
        alice = sorted(int(input()) for _ in range(a))
        bob = sorted(int(input()) for _ in range(b))
        solvable = sorted(set(alice) | set(bob))
        state = []
        for p in solvable:
            can_alice = p in alice
            can_bob = p in bob
            if can_alice and can_bob:
                state.append(2)
            elif can_alice:
                state.append(0)
            elif can_bob:
                state.append(1)
        dp_a, dp_b = INF, INF
        for i, s in enumerate(state):
            if i == 0:
                if s == 0:
                    dp_a = 0
                elif s == 1:
                    dp_b = 0
                else:
                    dp_a = 0
                    dp_b = 0
                continue
            temp_a, temp_b = INF, INF
            if s == 0 or s == 2:
                temp_a = min(dp_a, dp_b + 1)
            if s == 1 or s == 2:
                temp_b = min(dp_b, dp_a + 1)
            dp_a, dp_b = temp_a, temp_b
        answer = min(dp_a, dp_b)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
