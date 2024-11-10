from itertools import combinations
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    n = int(input())
    mapping = {}
    for _ in range(n):
        x, _, y = [input() for _ in range(3)]
        mapping[x] = y
    T = int(input())
    answers = []
    for _ in range(T):
        K = int(input())
        sentence = [input() for _ in range(K)]
        translated = ' '.join([mapping[word] for word in sentence])
        answer = translated
        answers.append(f"{answer}")
    print(*answers, sep="\n")