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
    MOD = 1000000007
    t = int(input())
    answers = []
    for hh in range(t):
        s = input()
        total_ways = 1
        i = 0
        n = len(s)
        while i < n:
            if s[i] != '?':
                c = s[i]
                j = i + 1
                while j < n and s[j] == c:
                    j += 1
                i = j
            else:
                start = i
                while i < n and s[i] == '?':
                    i += 1
                end = i
                k = end - start
                left_char = s[start - 1] if start > 0 and s[start - 1] != '?' else None
                right_char = s[end] if end < n and s[end] != '?' else None
                if left_char and right_char:
                    if left_char == right_char:
                        ways = 1
                    else:
                        ways = k + 1
                else:
                    ways = 1
                total_ways = (total_ways * ways) % MOD
        answer = total_ways
        answers.append(f"{answer}")
    print(*answers, sep="\n")