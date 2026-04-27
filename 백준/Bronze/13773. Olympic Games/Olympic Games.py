from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30

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
    canceled_years = list(range(1914, 1919)) + list(range(1939, 1946))
    no_city_chosen_years = {2024, 2028}
    answers = []
    for hh in range(t):
        year = int(input())
        if year == 0:
            break

        if year < 1896:
            answers.append(f"{year} No summer games")
        elif year >= 1896 and (year - 1896) % 4 != 0:
            answers.append(f"{year} No summer games")
        elif year in canceled_years:
            answers.append(f"{year} Games cancelled")
        elif year in no_city_chosen_years:
            answers.append(f"{year} No city yet chosen")
        else:
            answers.append(f"{year} Summer Olympics")
    print(*answers, sep="\n")