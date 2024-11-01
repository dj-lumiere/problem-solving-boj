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
    t = int(input())
    answers = []
    for case_num in range(1, t + 1):
        n = int(input())
        books = [int(input()) for _ in range(n)]
        alex_books = sorted([books[i] for i in range(n) if books[i] % 2 != 0])
        bob_books = sorted([books[i] for i in range(n) if books[i] % 2 == 0], reverse=True)
        answer = []
        alex_idx, bob_idx = 0, 0
        for i in range(n):
            if books[i] % 2 != 0:
                answer.append(alex_books[alex_idx])
                alex_idx += 1
            else:
                answer.append(bob_books[bob_idx])
                bob_idx += 1
        answers.append(f"Case #{case_num}: " + " ".join(map(str, answer)))
    print(*answers, sep="\n")