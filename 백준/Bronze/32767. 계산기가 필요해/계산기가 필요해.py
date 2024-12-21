# 32767번 계산기가 필요해
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
        num1 = float(input())
        op1 = input()
        num2 = float(input())
        op2 = input()
        num3 = float(input())
        if op1 == '+':
            res1 = num1 + num2
        elif op1 == '-':
            res1 = num1 - num2
        elif op1 == '*':
            res1 = num1 * num2
        elif op1 == '/':
            res1 = num1 / num2
        if op2 == '+':
            res2 = res1 + num3
        elif op2 == '-':
            res2 = res1 - num3
        elif op2 == '*':
            res2 = res1 * num3
        elif op2 == '/':
            res2 = res1 / num3
        rounded_result = precise_round(int(res2 * 10000), 10000, 3)
        answer = f'''=================
|SASA CALCULATOR|
|{rounded_result: >15}|
-----------------
|               |
| AC         /  |
| 7  8  9    *  |
| 4  5  6    -  |
| 1  2  3    +  |
|    0  .    =  |
================='''
        answers.append(f"{answer}")
    print(*answers, sep="\n")