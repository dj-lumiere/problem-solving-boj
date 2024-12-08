from fractions import Fraction
from sys import stderr, stdout


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
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for _ in range(t):
        n = int(input())
        x = int(input())
        y = int(input())
        V = [int(input()) for _ in range(n)]
        if len(V) < n:
            # Not enough speed values
            answers.append("-1")
            continue
        min_ti = min(Fraction(x, V[i]) for i in range(n - 1))
        your_time0 = Fraction(x, V[-1])
        if your_time0 < min_ti:
            answers.append("0")
            continue
        left, right = 1, y
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            remaining = x - mid
            if remaining <= 0:
                your_time = Fraction(1, 1)
            else:
                your_time = Fraction(1, 1) + Fraction(remaining, V[-1])
            if your_time < min_ti:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        if answer != -1:
            answers.append(str(answer))
        else:
            # Check if using booster at max Y
            remaining = x - y
            if remaining <= 0:
                your_time = Fraction(1, 1)
            else:
                your_time = Fraction(1, 1) + Fraction(remaining, V[-1])
            if your_time < min_ti:
                answers.append(str(y))
            else:
                answers.append("-1")
    print(*answers, sep="\n")