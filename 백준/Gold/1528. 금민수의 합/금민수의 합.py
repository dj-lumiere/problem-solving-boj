from collections import deque
from heapq import heapify, heappop, heappush
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
    MOD = 998_244_353
    t = 1
    answers = []
    for hh in range(1, t + 1):
        kummin_numbers = []
        for i in range(1, 7):
            for j in range(1 << i):
                kummin_numbers.append(int(bin(j)[2:].zfill(i).replace("0", "4").replace("1", "7")))
        # eprint(kummin_numbers)
        dp_table = [INF for _ in range(10 ** 6 + 1)]
        last_number = [INF for _ in range(10 ** 6 + 1)]
        bfs_queue = deque([(0, 0, 0)])
        visited = set()
        n = int(input())
        heap_count = 0
        while bfs_queue:
            length, current, last = bfs_queue.popleft()
            heap_count += 1
            current *= -1
            # eprint(length, current, last)
            # heap_count[current] += 1
            # eprint(current, last, length)
            for kummin_number in kummin_numbers:
                if current + kummin_number > 10 ** 6:
                    continue
                if dp_table[current + kummin_number] > length + 1 and last_number[
                    current + kummin_number] > kummin_number:
                    if (length + 1, kummin_number, current + kummin_number) in visited:
                        continue
                    dp_table[current + kummin_number] = length + 1
                    last_number[current + kummin_number] = kummin_number
                    visited.add((length + 1, kummin_number, current + kummin_number))
                    bfs_queue.append((length + 1, -(current + kummin_number), kummin_number))
                    continue
        # eprint(heap_count)
        # with open("output.txt", "w") as g:
        #     fprint(dp_table, file=g)
        # with open("output2.txt", "w") as g:
        #     fprint(last_number, file=g)
        # eprint(max(i for i in dp_table if i != INF))
        answer = []
        # eprint(dp_table[n])
        current_number = n
        while True:
            # eprint(current_number)
            if current_number == 0:
                break
            if last_number[current_number] == INF:
                answer = [-1]
                break
            answer.append(last_number[current_number])
            # eprint(answer)
            current_number -= last_number[current_number]
        # eprint(answer)
        answer.sort()
        answers.append(" ".join(map(str, answer)))
    print(*answers, sep="\n")