from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdin, stdout, stderr

getcontext().prec = 30

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    t = 10 ** 18
    answers = []
    sample = 1
    for hh in range(t):
        w, d = int(input()), int(input())
        if w == 0 and d == 0:
            break
        ratio = d / w
        age = 5730 * (Decimal(Decimal(810) / Decimal(ratio)).ln() / Decimal(2).ln())
        age_int = int(age.to_integral_value(rounding='ROUND_HALF_UP'))
        if age_int < 10000:
            remainder = age_int % 100
            if remainder >= 50:
                age_int = age_int - remainder + 100
            else:
                age_int = age_int - remainder
        else:
            remainder = age_int % 1000
            if remainder >= 500:
                age_int = age_int - remainder + 1000
            else:
                age_int = age_int - remainder
        answer = f"Sample #{sample}\nThe approximate age is {age_int} years.\n"
        answers.append(answer)
        sample += 1
    print(*answers, sep="\n")