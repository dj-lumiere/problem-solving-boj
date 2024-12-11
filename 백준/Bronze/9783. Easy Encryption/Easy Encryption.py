from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    answers = []
    t = 1
    for _ in range(t):
        s = input()
        encrypted = ''
        for c in s:
            if 'a' <= c <= 'z':
                encrypted += f"{ord(c) - 96:02}"
            elif 'A' <= c <= 'Z':
                encrypted += f"{ord(c) - 38:02}"
            elif '0' <= c <= '9':
                encrypted += f"#{c}"
            else:
                encrypted += c
        answer = encrypted
        answers.append(f"{answer}")
    print(*answers, sep="\n")