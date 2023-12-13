# 10909 Quaternion inverse

from math import gcd
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def sol(a, b, c, d, M):
    """
    sy.solve([a*w-b*x-c*y-d*z-1, a*x+b*w+c*z-d*y, a*y-b*z+c*w+d*x, a*z+b*y-c*x+d*w], [w, x, y, z])
    -> {w: a/(a**2 + b**2 + c**2 + d**2), x: -b/(a**2 + b**2 + c**2 + d**2), y: -c/(a**2 + b**2 + c**2 + d**2), z: -d/(a**2 + b**2 + c**2 + d**2)}
    """
    e = a**2 + b**2 + c**2 + d**2
    g = gcd(e, M)
    if g != 1:
        return 0, 0, 0, 0
    e %= M
    e_inverse = pow(e, -1, M)
    return a * e_inverse % M, -b * e_inverse % M, -c * e_inverse % M, -d * e_inverse % M


M, T = map(int, input().split())
for _ in range(T):
    print(*sol(*map(int, input().split()), M))
