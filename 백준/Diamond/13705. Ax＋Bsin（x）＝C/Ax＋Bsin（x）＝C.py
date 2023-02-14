# 13705 Ax+Bsin(x)=C
from decimal import Decimal, getcontext
from math import factorial
from time import sleep

getcontext().prec = 40

A, B, C = list(map(Decimal, input().split(" ")))
pi = Decimal(
    "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
)
error = Decimal("0.0000000000000000000000000000000000000000000000000000000000001")

x_memo = [Decimal(C) / Decimal(A + B), Decimal("100000.0")]

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
            value_sub = x**i / factorial(i)
            value += value_sub
        elif i % 4 == 3:
            value_sub = Decimal(-1) * x**i / factorial(i)
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
            value_sub = x**i / factorial(i)
            value += value_sub
        elif i % 4 == 2:
            value_sub = Decimal(-1) * x**i / factorial(i)
            value += value_sub
        if i % 2 == 0 and (-1 * error < value_sub < error or value_sub == Decimal("0")):
            return sign * value
        else:
            i += 1


def newton_rhapson(x: Decimal) -> Decimal:
    return x - Decimal((A * x + B * sin(x) - C) / (A + B * cos(x)))

counter = 0
while True:
    x_memo[(counter + 1) % 2] = newton_rhapson(x_memo[counter % 2])
    counter += 1
    if not int((x_memo[0] - x_memo[1])*Decimal(10**15)):
        solution = int((x_memo[counter % 2])*Decimal(10**7))
        if solution % 10 < 5:
            solution //= 10
        else:
            solution //= 10
            solution += 1
        solution_int, solution_frac = divmod(solution, 1000000)
        print(f"{solution_int}.{solution_frac:0>6}")
        break
