from sys import stderr, stdout

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
    for hh in range(t):
        n = int(input())
        balloons = list(map(int, [input() for _ in range(n)]))
        balloons_list = list(range(1, n + 1))
        current = 0
        answer_sequence = []
        for _ in range(n):
            answer_sequence.append(balloons_list.pop(current))
            if not balloons_list:
                break
            move = balloons[answer_sequence[-1] - 1]
            if move > 0:
                current = (current + move - 1) % len(balloons_list)
            else:
                current = (current + move) % len(balloons_list)
        answer = ' '.join(map(str, answer_sequence))
        answers.append(f"{answer}")
    print(*answers, sep="\n")