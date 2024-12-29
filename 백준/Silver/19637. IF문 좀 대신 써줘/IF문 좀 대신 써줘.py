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
        n, m = (int(input()) for _ in range(2))
        max_powers = []
        names = []
        for _ in range(n):
            name = input()
            power = int(input())
            max_powers.append(power)
            names.append(name)
        query_powers = [int(input()) for _ in range(m)]
        result = []
        for q in query_powers:
            left = 0
            right = n - 1
            ans_idx = n - 1
            while left <= right:
                mid = (left + right) // 2
                if max_powers[mid] >= q:
                    ans_idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            result.append(names[ans_idx])
        answer = "\n".join(result)
        answers.append(f"{answer}")
    print(*answers, sep="\n")