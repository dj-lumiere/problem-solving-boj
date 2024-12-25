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
        word = input()
        n = len(word)
        answer = -1
        for root_len in range(1, n // 2 + 1):
            if n % root_len != 0:
                continue
            candidate = word[:root_len]
            candidate_count = [0] * 26
            for c in candidate:
                candidate_count[ord(c) - 97] += 1
            valid = True
            for i in range(0, n, root_len):
                substring = word[i:i + root_len]
                substring_count = [0] * 26
                for c in substring:
                    substring_count[ord(c) - 97] += 1
                if substring_count != candidate_count:
                    valid = False
                    break
            if valid:
                answer = candidate
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")