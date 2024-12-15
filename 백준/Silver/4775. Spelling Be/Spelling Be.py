
# 문제 번호: 4775번
# 문제 제목: Spelling Be 다국어

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
        dictionary = set()
        for _ in range(n):
            dictionary.add(input())
        m = int(input())
        for email_num in range(1, m + 1):
            unknown_words = []
            while True:
                word = input()
                if word == "-1":
                    break
                if word not in dictionary:
                    unknown_words.append(word)
            if not unknown_words:
                answer = f"Email {email_num} is spelled correctly."
            else:
                answer = f"Email {email_num} is not spelled correctly.\n" + "\n".join(unknown_words)
            answers.append(answer)
        answers.append("End of Output")
    print(*answers, sep="\n")
