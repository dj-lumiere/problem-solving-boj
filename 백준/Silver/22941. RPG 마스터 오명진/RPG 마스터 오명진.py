from os import write

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    for hh in range(t):
        h1, a1, h2, a2, p, s = [int(input()) for _ in range(6)]
        answer = "gg"
        maou_attacks_before = (h2 - p + a1 - 1) // a1
        h2 -= maou_attacks_before * a1
        if 1 <= h2 <= p:
            h2 += s
        maou_attacks_after = (h2 + a1 - 1) // a1
        maou_attacks = maou_attacks_after + maou_attacks_before
        yuusha_attacks = (h1 + a2 - 1) // a2
        eprint(maou_attacks_after, maou_attacks_before, yuusha_attacks)
        if maou_attacks <= yuusha_attacks:
            answer = "Victory!"
        answers.append(f"{answer}")
    print(answers)