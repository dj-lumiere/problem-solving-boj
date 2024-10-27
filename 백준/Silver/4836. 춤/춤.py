from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
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
    t = INF
    answers = []
    for hh in range(t):
        dance = input()
        if dance is None:
            break
        steps = dance.split()
        rules_broken = []
        invalid_dips = []
        for i, step in enumerate(steps):
            if step == "dip":
                valid = False
                if i >= 1 and steps[i - 1] == "jiggle":
                    valid = True
                if i >= 2 and steps[i - 2] == "jiggle":
                    valid = True
                if i + 1 < len(steps) and steps[i + 1] == "twirl":
                    valid = True
                if not valid:
                    rules_broken.append(1)
                    invalid_dips.append(i)
        if 'dip' not in steps:
            rules_broken.append(5)
        if steps[-3:] != ["clap", "stomp", "clap"]:
            rules_broken.append(2)
        if 'twirl' in steps and 'hop' not in steps:
            rules_broken.append(3)
        if steps[0] == 'jiggle':
            rules_broken.append(4)
        if invalid_dips:
            for idx in invalid_dips:
                steps[idx] = "DIP"
            dance = " ".join(steps)
        rules_broken = sorted(set(rules_broken))
        if not rules_broken:
            answer = f"form ok: {dance}"
        elif len(rules_broken) == 1:
            answer = f"form error {rules_broken[0]}: {dance}"
        else:
            error_str = ", ".join(map(str, rules_broken[:-1])) + f" and {rules_broken[-1]}"
            answer = f"form errors {error_str}: {dance}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")