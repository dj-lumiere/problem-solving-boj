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
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    tc_end = False
    for hh in range(t):
        tour_info = []
        answer = 0
        while True:
            something = input()
            eprint(something)
            if something == "#":
                tc_end = True
                break
            if something == "0":
                break
            _, _, ActualMiles, ClassCode = something.split()
            tour_info.append((int(ActualMiles), ClassCode))
        if tc_end:
            break
        answer = 0
        for miles, code in tour_info:
            mileage = miles
            if code == "F":
                mileage *= 2
            elif code == "B":
                mileage += (mileage + 1) // 2
            if mileage < 500 and code == "Y":
                mileage = 500
            answer += mileage
        answers.append(f"{answer}")
    print(*answers, sep="\n")