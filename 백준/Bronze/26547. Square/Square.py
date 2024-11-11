from decimal import Decimal
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
    t = int(input())
    answers = []
    for hh in range(t):
        word = input()
        k = len(word)
        square = []
        for i in range(k):
            if i == 0:
                line = word
            elif i == k - 1:
                line = word[::-1]
            else:
                line = word[i] + ' ' * (k - 2) + word[k - 1 - i]
            square.append(line)
        answer = '\n'.join(square)
        answers.append(f"{answer}")
    print(*answers, sep="\n")