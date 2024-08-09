from decimal import Decimal, getcontext
from math import factorial
from sys import stdout, stderr

getcontext().prec = 40

pi = Decimal(
    "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
)
error = Decimal("1e-20")


def sin(x: Decimal) -> Decimal:
    sign = 1
    if not (0 <= x <= pi / 2):
        x = x - (x // (2 * pi)) * 2 * pi
        if x >= Decimal(1.5) * pi:
            x = 2 * pi - x
            sign = -1
        elif x >= pi:
            x -= pi
            sign = -1
        elif x >= Decimal(0.5) * pi:
            x = pi - x
    i = 0
    value: Decimal = Decimal(0)
    while True:
        value_sub = Decimal(0)
        if i % 4 == 1:
            value_sub = x ** i / factorial(i)
            value += value_sub
        elif i % 4 == 3:
            value_sub = Decimal(-1) * x ** i / factorial(i)
            value += value_sub
        if i % 2 == 1 and (-1 * error < value_sub < error or value_sub == Decimal("0")):
            return sign * value
        else:
            i += 1


def cos(x: Decimal) -> Decimal:
    sign = 1
    if not (0 <= x <= pi / 2):
        x = x - (x // (2 * pi)) * 2 * pi
        if x >= Decimal(1.5) * pi:
            x = 2 * pi - x
        elif x >= pi:
            x -= pi
            sign = -1
        elif x >= Decimal(0.5) * pi:
            x = pi - x
            sign = -1
    i = 0
    value: Decimal = Decimal(0)
    while True:
        value_sub = Decimal(0)
        if i % 4 == 0:
            value_sub = x ** i / factorial(i)
            value += value_sub
        elif i % 4 == 2:
            value_sub = Decimal(-1) * x ** i / factorial(i)
            value += value_sub
        if i % 2 == 0 and (-1 * error < value_sub < error or value_sub == Decimal("0")):
            return sign * value
        else:
            i += 1


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    for hh in range(t):
        l, n, c = (Decimal(input()) for _ in range(3))
        if l < 0 and n < 0 and c < 0:
            break
        l_prime = (1 + n * c) * l
        if l_prime == l:
            result = 0
        else:
            f = lambda x: sin(x) / x - (1 / (1 + n * c))
            fp = lambda x: -sin(x) / x ** 2 + cos(x) / x
            theta = pi / 4
            while True:
                next_theta = theta - f(theta) / fp(theta)
                if abs(theta - next_theta) < error:
                    break
                theta = next_theta
            r = l_prime / 2 / theta
            result = r * (1 - cos(theta))
        answer = f"{result:.3f}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
