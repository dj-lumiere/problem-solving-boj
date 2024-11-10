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
    t = 1
    answers = []
    for hh in range(t):
        A, B, C = int(input()), int(input()), int(input())
        if B == 0:
            if C == 0:
                answer = "1"
            else:
                answer = "NIKAD"
        elif B == 1:
            lenC = len(str(C)) if C != 0 else 1
            if A % (10 ** lenC) == C:
                answer = "1"
            else:
                answer = "NIKAD"
        else:
            lenC = len(str(C)) if C != 0 else 1
            mod = 10 ** lenC
            target = C
            current = (A * B) % mod
            presses = 1
            if current == target:
                answer = "1"
            else:
                visited = set()
                visited.add(current)
                while True:
                    current = (current * B) % mod
                    presses += 1
                    if current == target:
                        answer = str(presses)
                        break
                    if current in visited:
                        answer = "NIKAD"
                        break
        answers.append(f"{answer}")
    print(*answers, sep="\n")