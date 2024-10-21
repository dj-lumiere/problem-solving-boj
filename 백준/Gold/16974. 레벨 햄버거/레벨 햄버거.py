from sys import setrecursionlimit, stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        N = int(input())
        M = int(input())
        stack = [(N, M)]
        answer = 0
        layer_count = lambda x: 4 * 2 ** x - 3
        patty_count = lambda x: 2 * 2 ** x - 1
        while stack:
            n, eaten_layer_count = stack.pop()
            if eaten_layer_count == 0:
                pass
            elif n == 0 and eaten_layer_count == 1:
                answer += 1
            elif n != 0 and eaten_layer_count == 1:
                pass
            elif eaten_layer_count == layer_count(n - 1) + 2:
                answer += patty_count(n - 1) + 1
            elif eaten_layer_count == layer_count(n):
                answer += patty_count(n)
            elif eaten_layer_count < layer_count(n - 1) + 2:
                stack.append((n - 1, eaten_layer_count - 1))
            else:
                answer += patty_count(n - 1) + 1
                stack.append((n - 1, eaten_layer_count - layer_count(n - 1) - 2))
        answers.append(answer)
    print(*answers, sep="\n")
