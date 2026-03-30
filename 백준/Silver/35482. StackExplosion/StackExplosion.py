import heapq
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_009
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        c = [int(input()) for _ in range(n)]
        m = [int(input()) for _ in range(n)]
        current_offset = 0
        leftover_memory = [(ci - mi, mi) for ci, mi in zip(c, m)]
        heapq.heapify(leftover_memory)
        while len(leftover_memory) > 0:
            curr = heapq.heappop(leftover_memory)
            if curr[0] - current_offset < 0:
                next_offset = (curr[1] + current_offset) // 2
                while len(leftover_memory) > 0:
                    nxt = heapq.heappop(leftover_memory)
                    if nxt[0] - current_offset < 0:
                        next_offset += (nxt[1] + current_offset) // 2
                    else:
                        heapq.heappush(leftover_memory, nxt)
                        break
                current_offset += next_offset
            else:
                heapq.heappush(leftover_memory, curr)
                break
        answer = n - len(leftover_memory)
        answers.append(answer)
    print(*answers, sep="\n")