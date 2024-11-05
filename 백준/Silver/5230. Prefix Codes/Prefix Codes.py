from itertools import permutations, combinations
from sys import stderr, stdout

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
    t = int(input())
    answers = []
    for hh in range(t):
        k = int(input())
        prefix_code = input()
        decoded = []
        for _ in range(k):
            code = input()
            node = 0
            decoded_str = ''
            for bit in code:
                if bit == '0':
                    node = 2 * node + 1
                else:
                    node = 2 * node + 2
                if node < len(prefix_code) and prefix_code[node] != '*':
                    decoded_str += prefix_code[node]
                    node = 0
            decoded.append(decoded_str)
        answer = ' '.join(decoded)
        answers.append(f"{answer}")
    print(*answers, sep="\n")