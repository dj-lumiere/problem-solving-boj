from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
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
    list_num = 1
    for hh in range(t):
        n = int(input())
        if n == 0:
            break
        counts = {}
        for _ in range(n):
            animal = input().split()[-1].lower()
            counts[animal] = counts.get(animal, 0) + 1
        sorted_animals = sorted(counts.keys())
        answer = f"List {list_num}:"
        for animal in sorted_animals:
            answer += f"\n{animal} | {counts[animal]}"
        answers.append(f"{answer}")
        list_num += 1
    print(*answers, sep="\n")