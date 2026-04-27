import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    for i in range(t):
        pass
    while True:
        d, m, y = int(input()), int(input()), int(input())
        if y == m == d == 0:
            break
        valid_dates = lambda y: [0, 31, 29 if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else 28, 31, 30, 31, 30, 31,
                                 31, 30, 31, 30, 31]
        is_invalid = False
        if m not in range(1, 13):
            is_invalid = True
        elif d not in range(1, valid_dates(y)[m] + 1):
            is_invalid = True
        answers.append(f"{'Invalid' if is_invalid else 'Valid'}")
    print(answers)