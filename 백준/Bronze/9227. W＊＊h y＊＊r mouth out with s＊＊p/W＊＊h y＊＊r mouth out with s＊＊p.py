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


with open(0, 'r', encoding="utf-8") as f:
    tokens = iter(f.read().splitlines())
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
        offensive_pairs = set()
        while True:
            pair = input()
            if pair == '##':
                break
            offensive_pairs.add(pair)
        paragraph_tokens = []
        while True:
            token = input()
            if token == '#':
                break
            paragraph_tokens.append(token)
        sanitized_paragraph = []
        for word in paragraph_tokens:
            new_word = list(word)
            i = 0
            while i <= len(word) - 4:
                substring = word[i:i + 4]
                if substring.isalpha():
                    pair = substring[0] + substring[3]
                    if pair in offensive_pairs:
                        new_word[i + 1] = '*'
                        new_word[i + 2] = '*'
                        i += 4
                        continue
                i += 1
            sanitized_word = ''.join(new_word)
            sanitized_paragraph.append(sanitized_word)
        answer = ' '.join(sanitized_paragraph)
        answers.append(f"{answer}")
    print(*answers, sep="\n")