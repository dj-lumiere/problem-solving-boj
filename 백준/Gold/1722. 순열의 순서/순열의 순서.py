from math import factorial
from sys import stdout, stderr


def find_rank(n, sequence):
    factorials = [factorial(i) for i in range(n)]
    left_number = list(range(1, n + 1))
    rank = 0
    for i, v in zip(reversed(range(n)), sequence):
        index = left_number.index(v)
        rank += factorials[i] * index
        left_number.pop(index)
    return rank


def find_permutation(n, rank):
    factorials = [factorial(i) for i in range(n)]
    left_number = list(range(1, n + 1))
    result = []
    for i, v in zip(reversed(range(n)), reversed(factorials)):
        pop_index = rank // v
        result.append(left_number.pop(pop_index))
        rank -= pop_index * v
    return result


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
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        q = int(input())
        if q == 1:
            rank = int(input()) - 1
            result = " ".join(map(str, find_permutation(n, rank)))
        elif q == 2:
            permutation = [int(input()) for _ in range(n)]
            result = f"{find_rank(n, permutation) + 1}"
        answer = f"{result}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
