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
    for hh in range(t):
        N = int(input())
        M = int(input())
        info_progress = [int(input()) for _ in range(3)]
        surveillance_progress = [int(input()) for _ in range(3)]
        current_states = {(-1, 0): 1}
        for day in range(N):
            next_states = {}
            for (prev_loc, total), cnt in current_states.items():
                for action in range(6):
                    if action < 3:
                        location = action
                        progress = info_progress[location]
                    else:
                        location = action - 3
                        progress = surveillance_progress[location]
                    if location == prev_loc:
                        progress = progress // 2
                    new_total = total + progress
                    new_prev_loc = location
                    key = (new_prev_loc, new_total)
                    if key in next_states:
                        next_states[key] += cnt
                    else:
                        next_states[key] = cnt
            current_states = next_states
        count = sum(cnt for (loc, total), cnt in current_states.items() if total >= M)
        answer = count
        answers.append(f"{answer}")
    print(*answers, sep="\n")