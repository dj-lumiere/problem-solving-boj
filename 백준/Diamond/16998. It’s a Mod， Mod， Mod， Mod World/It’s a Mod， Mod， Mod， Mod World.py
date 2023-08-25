# 16998 It’s a Mod, Mod, Mod, Mod World
from sys import stdin
from math import gcd


def input():
    return stdin.readline().strip()


def find_result(p, q, n):
    """sum(pi // q for i in range(1, n + 1))"""
    if not p or not n:
        return 0
    if p >= q:
        return n * (n + 1) // 2 * (p // q) + find_result(p % q, q, n)
    return n * (p * n // q) + n // q - find_result(q, p, p * n // q)


W = int(input())
for _ in range(W):
    p, q, n = map(int, input().split(" "))
    g = gcd(p, q)
    print(n * (n + 1) // 2 * p - q * find_result(p // g, q // g, n))