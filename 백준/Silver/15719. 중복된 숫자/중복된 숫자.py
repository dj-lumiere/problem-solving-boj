from sys import stderr, stdout

with open(0, 'r') as f:
    input = lambda: f.read(1)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = 0
        while True:
            letter = input()
            if letter == " ":
                break
            if letter == "":
                break
            if letter == "\n":
                break
            n *= 10
            n += int(letter)
        answer = -(n * (n - 1) // 2)
        x = 0
        for _ in range(n):
            x = 0
            while True:
                letter = input()
                if letter == "":
                    break
                if letter == " ":
                    break
                if letter == "\n":
                    break
                x *= 10
                x += int(letter)
            answer += x
        answers.append(f"{answer}")
    print(*answers, sep="\n")