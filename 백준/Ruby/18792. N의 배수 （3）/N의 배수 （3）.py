from math import gcd
from sys import stderr, stdout


def find_t(p, T, d, u, v):
    l = u * pow(d, -1, p) % p
    h = p + (v * pow(d, -1, p) % p)
    while l + 1 != h:
        m = (l + h) // 2
        if T[m * d % p]:
            l = m
        else:
            h = m
    return h * d % p


def egz_prime(p, a):
    k = sorted(range(2 * p - 1), key=lambda x: a[x] % p)
    L = [False for _ in range(2 * p - 1)]
    for i in range(1, p):
        if a[k[i]] % p == a[k[i + p - 1]] % p:
            for j in range(i, i + p):
                L[k[j]] = True
            return L

    s = sum(a[k[i]] for i in range(p)) % p
    T = [False for _ in range(p)]
    P = [None for _ in range(p)]
    T[s] = True

    for i in range(1, p):
        if T[0]:
            break
        t_i = find_t(p, T, (a[k[p + i - 1]] - a[k[i]]) % p, s, 0)
        T[t_i] = True
        P[t_i] = i

    c = 0
    for i in range(p):
        L[k[i]] = 1
    while s != c:
        i = P[c]
        L[k[i + p - 1]] = True
        L[k[i]] = False
        c = (c - (a[k[i + p - 1]] - a[k[i]])) % p
    return L


def egz_composite(p, q, a):
    S = list(range(p - 1))
    T = [None for _ in range(2 * q - 1)]
    for i in range(2 * q - 1):
        S += [(i + 1) * p + j - 1 for j in range(p)]
        ret = egz(p, [a[s] for s in S])
        T[i] = [S[j] for j in range(2 * p - 1) if ret[j]]
        S = [S[j] for j in range(2 * p - 1) if not ret[j]]
    L = [False for _ in range(2 * p * q - 1)]
    ret = egz(q, [sum(a[t] for t in T[i]) // p for i in range(2 * q - 1)])

    for i in range(2 * q - 1):
        if ret[i]:
            for j in T[i]:
                L[j] = True
    return L


def egz(n, a):
    if n == 1:
        return [True]
    for i in range(2, n):
        if n % i == 0:
            return egz_composite(i, n // i, a)
    return egz_prime(n, a)


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    answers = []
    t = 1
    for hh in range(t):
        n = int(input())
        a = [int(input()) for _ in range(2 * n - 1)]
        egz_list = egz(n, a)
        answer = " ".join(map(str, [v for i, v in enumerate(a) if egz_list[i]]))
        answers.append(f"{answer}")
    print(*answers, sep="\n")
