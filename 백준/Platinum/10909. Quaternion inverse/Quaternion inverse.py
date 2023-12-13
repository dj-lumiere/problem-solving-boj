# 10909 Quaternion inverse

from math import gcd
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def sol(M, a, b, c, d):
    e = a**2 + b**2 + c**2 + d**2
    g = gcd(e, M)
    if g != 1:
        return 0, 0, 0, 0
    e %= M
    e_inverse = pow(e, -1, M)
    return a * e_inverse % M, -b * e_inverse % M, -c * e_inverse % M, -d * e_inverse % M


M, T = map(int, input().split())
for _ in range(T):
    print(*sol(M, *map(int, input().split())))


"""
import sympy as sy

a1, b1, c1, d1, a2, b2, c2, d2 = sy.symbols("a1 b1 c1 d1 a2 b2 c2 d2")
solution = sy.solve(
    [
        a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2 - 1,
        a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
        a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
        a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
    ],
    [a2, b2, c2, d2],
)
print(solution) # {a2: a1/(a1**2 + b1**2 + c1**2 + d1**2), b2: -b1/(a1**2 + b1**2 + c1**2 + d1**2), c2: -c1/(a1**2 + b1**2 + c1**2 + d1**2), d2: -d1/(a1**2 + b1**2 + c1**2 + d1**2)}
"""