from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        m = int(input())
        board = [input() for _ in range(n)]
        mbti_set = {"ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP",
                    "ESTJ", "ESFJ", "ENFJ", "ENTJ"}
        total = 0
        for i in range(n):
            for j in range(m):
                for dx, dy in DELTA:
                    s = ''
                    for k in range(4):
                        ni, nj = i + dx * k, j + dy * k
                        if 0 <= ni < n and 0 <= nj < m:
                            s += board[ni][nj]
                        else:
                            break
                    if len(s) == 4 and s in mbti_set:
                        total += 1
        answer = total
        answers.append(f"{answer}")
    print(*answers, sep="\n")