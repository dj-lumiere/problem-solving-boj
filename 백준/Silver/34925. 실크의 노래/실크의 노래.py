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
        h = int(input())
        s = int(input())
        answer = 0
        if h <= 2:
            answer = 1
        elif h >= 5 and h % 2 == 1:
            answer += (h - 3) // 2
            # 3 1 ! 4 2 ! 5...
            answer += (s // 2) * 3
            if s % 2 == 1:
                # 3 1 ! 4 2 0
                answer += 3
            else:
                # 3 1 -1
                answer += 2
        elif h >= 5 and h % 2 == 0:
            answer += (h - 4) // 2
            # 4 2 ! 5 3 1 !...
            answer += (s // 2) * 3
            if s % 2 == 1:
                # 4 2 ! 5 3 1 -1
                answer += 4
            else:
                # 4 2 0
                answer += 2
        elif h == 3:
            # 3 1 3 1 -1
            answer = s + 2
        elif h == 4:
            # 4 2 ! 4 2 ! 4 2 ! 4 2 0
            answer = s + 2
        answers.append(answer)
    print(*answers, sep="\n")
