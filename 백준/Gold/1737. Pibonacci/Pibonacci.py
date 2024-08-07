from math import pi
from sys import stdout, stderr

pibonacci_dict = {}


def pibonacci(n):
    if 0 <= n <= pi:
        return 1
    if 0 <= n - 1 <= pi:
        x = 1
    elif n - 1 in pibonacci_dict:
        x = pibonacci_dict[n - 1]
    else:
        x = pibonacci(n - 1)
        pibonacci_dict[n - 1] = x
    if 0 <= n - pi <= pi:
        y = 1
    elif n - pi in pibonacci_dict:
        y = pibonacci_dict[n - pi]
    else:
        y = pibonacci(n - pi)
        pibonacci_dict[n - pi] = y
    return (x + y) % 1000000000000000000


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        answer = pibonacci(n)
        eprint(len(pibonacci_dict))
        answers.append(f"{answer}")
    print(*answers, sep="\n")
