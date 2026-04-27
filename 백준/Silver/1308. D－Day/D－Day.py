import os
import datetime

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        y1, m1, d1 = [int(input()) for _ in range(3)]
        y2, m2, d2 = [int(input()) for _ in range(3)]
        if y2 - y1 > 1000 or (y2 - y1 == 1000 and (m2, d2) >= (m1, d1)):
            answers[i] = "gg"
            continue
        date1 = datetime.date(y1, m1, d1)
        date2 = datetime.date(y2, m2, d2)
        answers[i] = f"D-{(date2 - date1) // datetime.timedelta(days=1)}"
    print(answers)