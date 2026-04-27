from sys import stderr, stdout


def get_reward(score):
    if score >= 125:
        return 4
    if score >= 95:
        return 3
    if score >= 65:
        return 2
    if score >= 35:
        return 1
    return 0


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
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        d = [int(input()) for _ in range(n)]
        reward = [0 for _ in range(5)]
        current_point = 0
        current_time = 0
        dice_increment = 1
        time_increment = 4
        for i, v in enumerate(d):
            if current_time > 240:
                reward[get_reward(current_point)] += 1
                current_time = 0
                current_point = 0
                dice_increment = 1
                time_increment = 4
            if v == 1:
                reward[get_reward(current_point)] += 1
                current_time = 0
                current_point = 0
                dice_increment = 1
                time_increment = 4
                continue
            elif v == 2:
                if dice_increment > 1:
                    dice_increment //= 2
                elif dice_increment == 1:
                    time_increment += 2
            elif v == 3:
                pass
            elif v == 4:
                current_time += 56
            elif v == 5:
                if time_increment > 1:
                    time_increment -= 1
            elif v == 6:
                if dice_increment < 32:
                    dice_increment *= 2
            current_point += dice_increment
            current_time += time_increment
        answer = "\n".join(map(str, reward[1:]))
        answers.append(answer)
    print(*answers, sep="\n")