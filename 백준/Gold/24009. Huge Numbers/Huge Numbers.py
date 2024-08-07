from functools import reduce
from math import factorial
from sys import stdout, stderr


def compute_euler_phi(limit):
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    phi_values = [i for i in range(limit + 1)]

    for i in range(2, limit + 1):
        if not is_prime[i]:
            continue
        for j in range(i, limit + 1, i):
            is_prime[j] = False
            phi_values[j] = (phi_values[j] * (i - 1)) // i
    return phi_values


def n_fact_mod_p(n, p):
    return reduce(lambda x, y: x * y % p, range(1, n + 1)) % p


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    euler_phi = compute_euler_phi(100001)
    for hh in range(t):
        a, n, p = int(input()), int(input()), int(input())
        if a == 1:
            answer = 1 % p
        elif p == 1:
            answer = 0
        elif n <= 5:
            answer = pow(a, factorial(n), p)
        else:
            answer = pow(a, n_fact_mod_p(n, euler_phi[p]) + euler_phi[p], p)
        answers.append(f"Case #{hh + 1}: {answer}")
    print(*answers, sep="\n")
