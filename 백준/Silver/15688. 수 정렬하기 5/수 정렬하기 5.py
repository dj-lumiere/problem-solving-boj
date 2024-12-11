from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    INF = 10 ** 18
    answers = []
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    numbers.sort()
    for num in numbers:
        answer = num
        answers.append(f"{answer}")
    print(*answers, sep="\n")