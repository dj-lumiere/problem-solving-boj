from collections import defaultdict, deque
from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for _ in range(t):
        N, L = int(input()), int(input())
        elimination_seq = [int(input()) for _ in range(L)]
        heifers = deque(range(1, N+1))
        seq = deque(elimination_seq)
        while len(heifers) > 1:
            count = seq.popleft()
            seq.append(count)
            heifers.rotate(- (count - 1))
            heifers.popleft()
        answer = heifers[0]
        answers.append(f"{answer}")
    print(*answers, sep="\n")