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
        size = 2 ** n
        cows = [int(input()) for _ in range(size)]
        total_distance = 0


        def sort_cows(cows):
            global total_distance
            if len(cows) == 1:
                return cows
            mid = len(cows) // 2
            left = sort_cows(cows[:mid])
            right = sort_cows(cows[mid:])
            if right < left:
                left, right = right, left
                total_distance += 2 * mid ** 2
            return left + right


        sorted_cows = sort_cows(cows)
        answer = f"{total_distance}"
        answer += "\n" + "\n".join(map(str, sorted_cows))
        answers.append(f"{answer}")
    print(*answers, sep="\n")